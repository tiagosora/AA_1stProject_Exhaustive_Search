import networkx as nx
import pickle
import random

def generate_and_save_graphs(num_vertices_list, percentage_list, seed, filename):
    
    random.seed(seed)
    graphs = {}
    
    for num_vertices in num_vertices_list:
        for percentage in percentage_list:
            
            G = nx.Graph()
            vertices = []
            
            for _ in range(num_vertices):
                while True:
                    x, y = random.randint(1, 100), random.randint(1, 100)
                    if all(((x - vertice_x)**2 + (y - vertice_y)**2) >= 2 for vertice_x, vertice_y in vertices):
                        vertices.append((x, y))
                        G.add_node((x, y))
                        break
                
            num_edges = int(num_vertices * (num_vertices - 1) // 2 * percentage)
            all_possible_edges = [(vertices[i], vertices[j]) for i in range(num_vertices) for j in range(i+1, num_vertices)]

            G.add_edges_from(random.sample(all_possible_edges, num_edges))
            nx.set_edge_attributes(G, {(u, v): random.randint(1, 10) for u, v in G.edges()}, 'weight')

            graphs[(num_vertices, percentage)] = G
        
    with open(filename, 'wb') as f:
        pickle.dump(graphs, f)

def compare_with_networkx(G, max_weight):

    networkx_matching = nx.max_weight_matching(G, maxcardinality = False)
    networkx_weight = sum(G[u][v]['weight'] for u, v in networkx_matching)

    if max_weight != networkx_weight:
        print("The maximum weighted matchings and weights differ.")
