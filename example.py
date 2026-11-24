import networkx as nx
import pandas as pd

G = nx.read_edgelist(
    "SS-Butterfly_weights.tsv",
    delimiter="\t",
    nodetype=str,
    data=(("weight", float),)
)

labels = pd.read_csv("SS-Butterfly_labels.tsv", sep="\t", header=None,
                     names=["node", "label"], dtype=str)
nx.set_node_attributes(G, dict(zip(labels["node"], labels["label"])), "label")

print("Graph statistics")
print("----------------")
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")

print(f"Density: {nx.density(G):.6f}")

if nx.is_directed(G):
    print(f"Directed graph: Yes")
    print(f"Weakly connected components: {nx.number_weakly_connected_components(G)}")
    print(f"Strongly connected components: {nx.number_strongly_connected_components(G)}")
else:
    print(f"Directed graph: No")
    print(f"Connected components: {nx.number_connected_components(G)}")

degrees = [d for _, d in G.degree()]

print(f"Average degree: {sum(degrees)/len(degrees):.2f}")
print(f"Maximum degree: {max(degrees)}")
print(f"Minimum degree: {min(degrees)}")

avg_clust = nx.average_clustering(G)                    # unweighted
avg_clust_w = nx.average_clustering(G, weight="weight") # weighted version
transitivity = nx.transitivity(G)                       # global clustering

print(f"Average clustering coefficient: {avg_clust:.4f}")
print(f"Weighted average clustering:    {avg_clust_w:.4f}")
print(f"Transitivity (global):          {transitivity:.4f}")


from networkx.algorithms.community import louvain_communities, modularity

comms = louvain_communities(G, weight="weight", seed=42)
Q = modularity(G, comms, weight="weight")

print(f"Number of communities: {len(comms)}")
print(f"Modularity: {Q:.4f}")
print(f"Community sizes: {sorted((len(c) for c in comms), reverse=True)}")

# Graph statistics
#----------------
# Number of nodes: 832
# Number of edges: 86528
# Density: 0.250301
# Directed graph: No
# Connected components: 1
# Average degree: 208.00
# Maximum degree: 530
# Minimum degree: 33
# Diameter: 4
# Radius: 2
# Average shortest path length: 1.804
# Average clustering coefficient: 0.5954
# Weighted average clustering:    0.0240
# Transitivity (global):          0.5641
# Number of communities: 7
# Modularity: 0.4365
# Community sizes: [172, 170, 160, 92, 84, 83, 71]
