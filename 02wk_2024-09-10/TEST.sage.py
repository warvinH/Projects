

# This file was *autogenerated* from the file TEST.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_6 = Integer(6); _sage_const_4 = Integer(4); _sage_const_5 = Integer(5); _sage_const_7 = Integer(7)# Tests 'weightedGraph' module which contains main code
# includes some code from week1 as well.
load('weightedGraph.sage')


# Example usage
# Define a graph; you can modify this to any graph you need
edges_3 = [(_sage_const_1 , _sage_const_2 ), (_sage_const_2 , _sage_const_3 ), (_sage_const_1 , _sage_const_3 )]
edges_7 = [(_sage_const_1 , _sage_const_2 ), (_sage_const_1 , _sage_const_6 ), (_sage_const_1 , _sage_const_4 ), (_sage_const_2 , _sage_const_3 ), (_sage_const_3 , _sage_const_4 ), (_sage_const_4 , _sage_const_5 ), (_sage_const_5 , _sage_const_6 )]
edges_7_alt = [(_sage_const_1 , _sage_const_2 ), (_sage_const_1 , _sage_const_6 ), (_sage_const_1 , _sage_const_5 ), (_sage_const_2 , _sage_const_3 ), (_sage_const_3 , _sage_const_4 ), (_sage_const_4 , _sage_const_5 ), (_sage_const_5 , _sage_const_6 )]
G1 = Graph(edges_3)
G2 = Graph(edges_7)
G3 = Graph(edges_7_alt)

# Assign random weights to edges
assign_random_weights(G1, _sage_const_1 , _sage_const_7 )
#weights = {1,2,3,4,5,6,7}
    #for edge in graph.edges():
        #weights[edge] = edge
        
    # Set edge labels using set_edge_label in a loop
    #for edge, weight in weights.items():
        #graph.set_edge_label(edge[0], edge[1], weight)
assign_random_weights(G2, _sage_const_1 , _sage_const_7 )
assign_random_weights(G3, _sage_const_1 , _sage_const_1 )

#G1
# Print the edge weights
print(f"Edge weights: {G1.edge_labels()}")
# Get the product of edge weights for each spanning tree
products1 = product_of_edges_in_spanning_trees(G1)
# Display the products
print(f"Products of edge weights for each spanning tree: {products1}")
print(f"Sum of the products: {sum(products1)}")
# Display matrix-tree
print("C3 Graph:")
print(G1.laplacian_matrix())
print("#SpanningTs: ", G1.spanning_trees_count())
# plot
plotG1 = G1.plot()
plotG1.save("week2G1.png")
print()

#G2
# Print the edge weights
print(f"Edge weights: {G2.edge_labels()}")
# Get the product of edge weights for each spanning tree
products2 = product_of_edges_in_spanning_trees(G2)
# Display the products
print(f"Products of edge weights for each spanning tree: {products2}")
print(f"Sum of the products: {sum(products2)}")
# Display matrix-tree
print("C6 + edge Graph:")
print(G2.laplacian_matrix())
print("#SpanningTs: ", G2.spanning_trees_count())
# plot
plotG2 = G2.plot()
plotG2.save("week2G2.png")
print()

#G3
# Print the edge weights
print(f"Edge weights: {G3.edge_labels()}")
# Get the product of edge weights for each spanning tree
products3 = product_of_edges_in_spanning_trees(G3)
# Display the products
print(f"Products of edge weights for each spanning tree: {products3}")
print(f"Sum of the products: {sum(products3)}")
# Display matrix-tree
print("C6 + edge(alt) Graph:")
print(G3.laplacian_matrix())
print("#SpanningTs: ", G3.spanning_trees_count())
# plot
plotG3 = G3.plot()
plotG3.save("week2G3.png")

