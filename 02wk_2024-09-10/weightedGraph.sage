# Name: Warvin Hassan
# Project: Graph Theory Project Week #2
# Instructor: Dr. Goyt
# Date: 09/10/2024 (Fall Semester)
##########################################################################
# This program will construct weighted graphs by randomly generating positive integers
# and assigning them to edges and then for each spanning tree of a given graph, we take the product of all the weights
# and then the sum of all the products of the spanning trees to find the value of the respective graph itself.
# This program will utilize the usage of functions, psuedo-random generators, and built in functions as necessary.
##########################################################################
import random
# Function to generate random integer weights for edges
def assign_random_weights(graph, min_weight, max_weight):
    weights = {}
    for edge in graph.edges():
        weights[edge] = random.randint(min_weight, max_weight)
        
    # Set edge labels using set_edge_label in a loop
    for edge, weight in weights.items():
        graph.set_edge_label(edge[0], edge[1], weight)

# Function to compute the product of edge weights for each spanning tree
def product_of_edges_in_spanning_trees(graph):
    # Ensure the graph is connected
    if not graph.is_connected():
        raise ValueError("The graph must be connected to find spanning trees.")
    
    # Get all spanning trees
    spanning_trees = graph.spanning_trees()
    
    # Initialize a list to store products of edge weights for each spanning tree
    products = []
    
    # Iterate through each spanning tree
    for tree in spanning_trees:
        product = 1
        for edge in tree.edges():
            # Determine edge format and retrieve vertices
            if isinstance(edge, tuple) and len(edge) == 2:
                u, v = edge
            else:
                u, v = edge[0], edge[1]  # Adjust according to actual edge format
            
            # Get the weight of the edge
            weight = graph.edge_label(u, v)  # Retrieve weight using edge_label
            product *= weight
        products.append(product)
    
    return products