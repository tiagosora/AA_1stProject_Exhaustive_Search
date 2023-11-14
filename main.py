from exhaustive_search import exhaustive_search
from utils import compare_with_networkx
from greedy_search import greedy_search

import pickle

def load_graphs(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
    
def main():
    graphs = load_graphs('graphs.pickle')

    run = ""
    # run = "exhaustive_search"
    run = "greedy_search"
    
    for (num_vertices, percentage), G in graphs.items():
        print(f"\nNumber of vertices: {num_vertices}, Percentage of edges: {percentage}")

        if run == "exhaustive_search" and num_vertices < 21:
            
            file = open(f"exhaustive_results/{num_vertices}_{percentage}_results", "w")
            
            _, max_weight, num_operations, time, num_solutions = exhaustive_search(G)
            results = f"Exhaustive Weight: {max_weight}, Time: {time}, Number of Operations: {num_operations}, Number of Solutions: {num_solutions}"
            print(results)
            
            compare_with_networkx(G, max_weight)

            file.write(results)

        elif run == "greedy_search":

            file = open(f"greedy_results/{num_vertices}_{percentage}_results", "w")

            _, max_weight, num_operations, time = greedy_search(G)
            results = f"Greedy Weight: {max_weight}, Time: {time}, Number of Operations: {num_operations}"
            print(results)

            file.write(results)


if __name__=="__main__":
    main()