"""
This implementation first calculates the number of incoming edges for each node in the input graph.
It then initializes a list of nodes with no incoming edges and a list to store the topologically sorted nodes.

It performs a depth-first search starting from each node with no incoming edges, adding each node to the sorted list and removing its outgoing edges.
If a node's incoming edge count reaches zero, it is added to the list of nodes with no incoming edges.
This process continues until all nodes have been added to the sorted list.

Finally, the implementation checks if a cycle exists in the graph by comparing the length of the sorted list to the number of nodes in the graph.
If the lengths are not equal, a cycle must exist and a ValueError is raised. Otherwise, the sorted list is returned.
"""


def topologicalSort(graph):
    # Create a dictionary to store the number of incoming edges for each node
    incoming_edges = {node: 0 for node in graph}
    # Calculate the number of incoming edges for each node
    for node in graph:
        for neighbor in graph[node]:
            incoming_edges[neighbor] += 1


    # Initialize a list to store the nodes with no incoming edges
    no_incoming_edges = [node for node in incoming_edges if incoming_edges[node] == 0]
    # Initialize a list to store the topologically sorted nodes
    sorted_nodes = []
    # Perform a depth-first search starting from each node with no incoming edges
    while no_incoming_edges:
        node = no_incoming_edges.pop()
        sorted_nodes.append(node)
        for neighbor in graph[node]:
            incoming_edges[neighbor] -= 1
            if incoming_edges[neighbor] == 0:
                no_incoming_edges.append(neighbor)
    # Check if a cycle exists in the graph
    if len(sorted_nodes) != len(graph):
        raise ValueError("Cycle detected in graph")
    return sorted_nodes


"""
This graph has four nodes (A, B, C, and D) and four edges (A to B, A to C, B to C, and B to D). The expected topologically sorted order for this graph is A, B, C, D.

When you run the above code, the topologicalSort function will be called with the graph dictionary as its input. 
The function will perform a topological sort on the graph and return a list of the sorted nodes.

The expected output for this example is:
"""
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': []
}

sorted_nodes = topologicalSort(graph)
print(sorted_nodes)
