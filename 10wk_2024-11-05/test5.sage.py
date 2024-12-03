

# This file was *autogenerated* from the file test5.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_5 = Integer(5); _sage_const_10 = Integer(10); _sage_const_4 = Integer(4); _sage_const_8 = Integer(8); _sage_const_2 = Integer(2); _sage_const_7 = Integer(7)
from itertools import permutations

def max_graph_value_and_assignments(graph, fixed_weights):
    edges = list(graph.edges(labels=False))
    
    # Separate fixed and unfixed edges
    fixed_edges = list(fixed_weights.keys())
    unfixed_edges = [e for e in edges if e not in fixed_edges]
    num_unfixed_edges = len(unfixed_edges)
    
    # Generate all permutations for the remaining unfixed edges
    all_weight_assignments = list(permutations(range(_sage_const_1 , num_unfixed_edges + _sage_const_1 )))
    
    max_graph_value = _sage_const_0 
    max_assignments = []
    all_results = []

    for i, unfixed_assignment in enumerate(all_weight_assignments, start=_sage_const_1 ):
        # Assign weights to unfixed edges
        edge_weights = {unfixed_edges[j]: unfixed_assignment[j] for j in range(num_unfixed_edges)}
        
        # Add the fixed weights to the current edge weight assignment
        edge_weights.update(fixed_weights)
        
        # Calculate the graph value for this assignment
        graph_value = _sage_const_0 
        for tree in graph.spanning_trees():
            tree_product = _sage_const_1 
            for edge in tree.edges(labels=False):
                tree_product *= edge_weights[edge]
            graph_value += tree_product
        
        # Track all assignments and their graph values
        all_results.append((f"Permutation {i}", unfixed_assignment, edge_weights, graph_value))
        
        # Update max graph value and track all permutations with this max value
        if graph_value > max_graph_value:
            max_graph_value = graph_value
            max_assignments = [i]  # Reset with the current permutation
        elif graph_value == max_graph_value:
            max_assignments.append(i)  # Add to list of max-value permutations
    
    return max_graph_value, max_assignments, all_results
    

# Usage
G = graphs.CompleteGraph(_sage_const_5 )
fixed_weights = {
    (_sage_const_0 , _sage_const_1 ): _sage_const_10 ,
    (_sage_const_0 ,_sage_const_4 ): _sage_const_8 ,
    (_sage_const_1 ,_sage_const_2 ): _sage_const_7 
}
max_value, max_permutations, all_assignments = max_graph_value_and_assignments(G, fixed_weights)

print("Max Graph Value:", max_value)
print("Permutations with Max Graph Value:", max_permutations)
print("All Assignments and Values:")
for label, assignment, edge_weights, value in all_assignments:
    print(f"{label}: {assignment} with Graph Value = {value}")
    print("Edge weights:", edge_weights)
    print()

