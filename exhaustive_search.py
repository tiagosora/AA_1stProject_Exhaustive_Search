from time import time

def exhaustive_search(G):
    def recursive_search(matching, weight, covered, start, max_possible_weight):
        nonlocal num_operations, num_solutions, max_matching, max_weight

        num_operations += 1
        if weight + max_possible_weight < max_weight:
            return
        
        num_operations += 1
        if start == len(all_edges):
            num_solutions += 1

            num_operations += 1
            if weight >= max_weight:
                num_operations += 2
                max_matching = set(matching)
                max_weight = weight

            return
        
        num_operations += 2
        u, v, edge_weight = all_edges[start]
        if u not in covered and v not in covered:

            num_operations += 3
            matching.add((u, v))
            covered.add(u)
            covered.add(v)

            recursive_search(matching, weight + edge_weight, covered, start + 1, max_possible_weight - edge_weight)

            num_operations += 3
            matching.remove((u, v))
            covered.remove(u)
            covered.remove(v)

        recursive_search(matching, weight, covered, start + 1, max_possible_weight - edge_weight)

    start_time = time()
    all_edges = sorted(G.edges(data='weight'), key=lambda x: x[2], reverse=True)
    max_possible_weight = sum(edge[2] for edge in all_edges)
    max_weight = 0
    max_matching = set()
    num_operations = 0
    num_solutions = 0

    recursive_search(set(), 0, set(), 0, max_possible_weight)
    end_time = time()

    return max_matching, max_weight, num_operations, end_time - start_time, num_solutions