import networkx as nx
import matplotlib.pyplot as plt

# Creating a simple knowledge graph

graph = nx.Graph()

# Adding topics
topics = [
    "Python",
    "Machine Learning",
    "AI",
    "Deep Learning",
    "Data Science"
]

for item in topics:
    graph.add_node(item)

# Connecting related topics
graph.add_edge("Python", "AI")
graph.add_edge("Python", "Data Science")
graph.add_edge("AI", "Machine Learning")
graph.add_edge("Machine Learning", "Deep Learning")

# Printing information
print("Topics present in the graph:")
for node in graph.nodes():
    print(node)

print("\nConnections between topics:")
for edge in graph.edges():
    print(edge)

# Displaying graph
plt.figure(figsize=(8, 6))

nx.draw(
    graph,
    with_labels=True,
    node_size=2800
)

plt.title("Simple Knowledge Graph Example")
plt.show()
