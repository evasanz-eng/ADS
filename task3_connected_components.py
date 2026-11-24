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




# other things worth studying
#Degree distribution: Which butterfly organisms have the most connections?
#Betweenness centrality: Which organisms act as bridges between different groups?
#Clustering coefficient: Are organisms connected to organisms that are also connected to each other?
#Community detection: Can you identify clusters of closely related butterfly organisms?