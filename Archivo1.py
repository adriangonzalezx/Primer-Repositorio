print("Hola mundo")
print ("jhola")
print ("adiosito")
print ("poooo")

# generame una funcion que me de un grafo en djisktra
import networkx as nx
import matplotlib.pyplot as plt

def generate_dijkstra_graph():
    # Create a new graph
    G = nx.Graph()

    # Add nodes to the graph
    G.add_nodes_from([1, 2, 3, 4, 5])

    # Add edges to the graph
    G.add_edge(1, 2, weight=3)
    G.add_edge(1, 3, weight=2)
    G.add_edge(2, 3, weight=1)
    G.add_edge(2, 4, weight=4)
    G.add_edge(3, 4, weight=2)
    G.add_edge(3, 5, weight=3)
    G.add_edge(4, 5, weight=1)

    # Compute the shortest path using Dijkstra's algorithm
    shortest_path = nx.dijkstra_path(G, 1, 5)

    # Print the shortest path
    print("Shortest path from node 1 to node 5:", shortest_path)

    # Visualize the graph
    nx.draw(G, with_labels=True)
    plt.show()

# Call the function to generate the graph
generate_dijkstra_graph()


