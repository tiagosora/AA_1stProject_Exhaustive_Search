from time import time

def greedy_search(G):
    start_time = time()
    all_edges = sorted(G.edges(data = True), key = lambda e: e[2]['weight'], reverse = True)
    matching = set()
    covered = set()
    max_weight = 0
    num_operations = 0 

    for u, v, data in all_edges:

        num_operations += 1
        if u not in covered and v not in covered:

            num_operations += 4
            covered.add(u)
            covered.add(v)
            matching.add((u, v))
            max_weight += data['weight']
    
    end_time = time()

    return matching, max_weight, num_operations, end_time - start_time