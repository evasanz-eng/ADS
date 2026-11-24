# Since there is 1 connected component (all nodes can be reached) and the graph is undirected, it makes no difference wether we use 
# breadth first search or depth first search

import networkx as nx
from example import G

# Find connected components
components = list(nx.connected_components(G))
print("Number of connected components:", len(components))

# Size of each component
for i, component in enumerate(components): # for each component
    print(f"Component {i+1}: {len(component)} nodes")
components = []
visited = set()
for node in G.nodes():
    if node not in visited:
        component = set()
        queue = [node]
        visited.add(node)

        while queue:
            current = queue.pop(0)
            component.add(current)

            for neighbor in G.neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        components.append(component)


#### CLUSTERING COEFFICIENT ####

#1. The clustering coefficient measures if the neighbours a node is connected to are also connected between each other.
#    The average clustering coefficient is calculated by averaging the local coefficients across all nodes in the network.
#    The coefficient ranges between 0 and 1. A value of 0 indicates that none of a node's neighbours are connected to each other, whereas a value of 1 indicates that all its neighbours are interconnected.

# 2. The objective of using this metric is to analyze the extent of local connectivity and determine if the network contains tightly interconnected groups.

# 3. In this scenario, this represents wether some organisms of butterfly are all similar (connected) or it is less local.
#    If the clustering coefficient is high, it shows a similar connectivity patterns between species, possibly emaning biological ressemblance.

# 4.
# Calculate local clustering coefficient for each node
clustering = nx.clustering(G, weight=None)

# Calculate average clustering coefficient
avg_clustering = nx.average_clustering(G, weight=None)

print("Clustering coefficient statistics")
print("----------------------------------")
print(f"Average clustering coefficient: {avg_clustering:.4f}")
print(f"Maximum clustering coefficient: {max(clustering.values()):.4f}")
print(f"Minimum clustering coefficient: {min(clustering.values()):.4f}")

# Sort nodes by clustering coefficient
sorted_clustering = sorted(
    clustering.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nTop 10 organisms by clustering coefficient")

for node, coefficient in sorted_clustering[:10]:
    label = G.nodes[node].get("label", node)
    print(f"{label}: {coefficient:.4f}")

#Clustering coefficient statistics
#----------------------------------
#Average clustering coefficient: 0.5954
#Maximum clustering coefficient: 0.9303
#Minimum clustering coefficient: 0.3728

#Top 10 organisms by clustering coefficient
#0.015727: 0.9303
#0.034699: 0.9132
#0.065361: 0.9034
#0.436401: 0.8899
#0.509266: 0.8820
#0.174339: 0.8510
#0.082452: 0.8468
#0.300119: 0.8454
#0.854803: 0.8390
#0.076795: 0.8369

#5. Analysis of results:
# On average, the neighbours are highly connected with each other, instead of having isolated neighbours. 
# The range between highest and lowest clustering coefficient is relatively low, which indicated that most nodes (organisms) have the same pattern of connectivity.
# We don't expect to find a few highly clustered organisms but rather a uniform network.  
