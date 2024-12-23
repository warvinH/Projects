from itertools import permutations

def max_graph_value_and_assignments(graph, fixed_weights):
    edges = list(graph.edges(labels=False))
    
    # Separate fixed and unfixed edges
    fixed_edges = list(fixed_weights.keys())
    unfixed_edges = [e for e in edges if e not in fixed_edges]
    num_unfixed_edges = len(unfixed_edges)
    
    # Identify all possible weights and remove those used for fixed edges
    total_weights = set(range(1, len(edges) + 1))
    used_weights = set(fixed_weights.values())
    unused_weights = list(total_weights - used_weights)
    
    # Generate all permutations for the remaining unfixed edges using unused weights only
    all_weight_assignments = list(permutations(unused_weights))
    
    max_graph_value = 0
    max_assignments = []
    all_results = []

    for i, unfixed_assignment in enumerate(all_weight_assignments, start=1):
        # Assign weights to unfixed edges only
        edge_weights = {unfixed_edges[j]: unfixed_assignment[j] for j in range(num_unfixed_edges)}
        
        # Add the fixed weights to the current edge weight assignment
        edge_weights.update(fixed_weights)
        
        # Calculate the graph value for this assignment
        graph_value = 0
        for tree in graph.spanning_trees():
            tree_product = 1
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
    #return max_graph_value

# Usage
#G = graphs.CompleteGraph(5)
G = Graph([(1,2), (2,3), (3,4), (4,5), (5,6), (6,1), (1,4)])
fixed_weights = {
    #(0, 1): 6, 
    #(0, 4): 8,
    #(1, 2): 7,
    #(3, 4): 9,
    #(2, 3): 10
}
max_value, max_permutations, all_assignments = max_graph_value_and_assignments(G, fixed_weights)
#max_value= max_graph_value_and_assignments(G, fixed_weights)

print("Max Graph Value:", max_value)
print("Permutations with Max Graph Value:", max_permutations)
print("All Assignments and Values:")
for label, assignment, edge_weights, value in all_assignments:
    print(f"{label}: {assignment} with Graph Value = {value}")
    print("Edge weights:", edge_weights)
    print()
