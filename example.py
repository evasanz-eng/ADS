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
