load('weightedGraphs4.sage')
load('weightedGraphs4b.sage')

# G1
G1 = graphs.CompleteGraph(3)

# Automatically assign weights and calculate Hamiltonian cycles for all permutations
all_cycles_data, all_weights_data = perm_weights(G1)

# Process the results for each permutation
total_sum_all_permutations = 0
max_sum_of_products = 0  # Initialize max_product to track the maximum product found
max_total= 0
p1=0
permutation_count = 1
total_graph_value = 0

for cycle_data, weights in zip(all_cycles_data, all_weights_data):
    print(f"Permutation {permutation_count}:")
    print(f"Edge Weights: {weights}")  # Print the edge weights for this permutation
    totSum = 0
    cycle_count = 1
    p1=0
    for cycle, cycle_weights, product in cycle_data:
        print(f"Cycle {cycle_count}: {cycle}, Weights: {cycle_weights}, Product of Weights: {product}")
        totSum += product
        total_graph_value += product
        cycle_count += 1
        for p in product_of_edges_in_spanning_trees(G1):
            p1+=p
    print(f"Sum of products for this permutation: {totSum}")
    print(f"Total Graph Value for this permutation: {total_graph_value}\n")
    print("tot",p1)
    max_sum_of_products = max(max_sum_of_products, totSum)
    max_total = max(total_graph_value,max_total)
    permutation_count += 1

print("Maximum Sum of Products from all permutations:", max_sum_of_products)
print(max_total)
print(f"#SpanningTs: {G1.spanning_trees_count()}")
