import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re

####### FIGURE 4

vertices = {
    1: (1, 2),
    2: (2, 2),
    4: (1, 1),
    3: (2, 1)
}
edges = {
    (1, 2): 3,
    (3, 4): 3,
    (1, 3): 4
}

for vertex, pos in vertices.items():
    plt.scatter(*pos)
    plt.text(pos[0], pos[1]+0.1, f'{vertex}', fontsize = 12, ha = 'center')

for (u, v), weight in edges.items():
    u_pos, v_pos = vertices[u], vertices[v]
    plt.plot([u_pos[0], v_pos[0]], [u_pos[1], v_pos[1]], 'black')
    mid_point = ((u_pos[0]+v_pos[0])/2, (u_pos[1]+v_pos[1])/2) #TODO fazer isot mais alto
    plt.text(mid_point[0], mid_point[1], str(weight), color = 'blue', fontsize = 12)

# plt.axis('off')
# plt.show()

def process_results(folder_path, algorithm_type):
    results = []

    for file_name in os.listdir(folder_path):

        vertices, edge_density = map(float, re.findall(r'(\d+)_([\d.]+)', file_name)[0])
        file_path = os.path.join(folder_path, file_name)

        with open(file_path, 'r') as file:

            for line in file:

                print(re.findall(r'[\d.]+e?[\+\-]?[\d]*', line))

                if algorithm_type  ==  'exhaustive':
                    weight, time, operations, _ = map(float, re.findall(r'[\d.]+e?[\+\-]?[\d]*', line))
                else:
                    weight, time, operations = map(float, re.findall(r'[\d.]+e?[\+\-]?[\d]*', line))

                results.append((vertices, edge_density, weight, time, operations, algorithm_type))

    return pd.DataFrame(results, columns = ['Vertices', 
                                          'Edge Density', 
                                          'Weight', 
                                          'Time', 
                                          'Operations', 
                                          'Algorithm'])

visualization = pd.concat([process_results('./exhaustive_results', 'exhaustive'), 
                                 process_results('./greedy_results', 'greedy')])

sns.set(style = "whitegrid")
plt.figure(figsize = (10, 6))
sns.scatterplot(data = visualization, 
                x = 'Vertices',
                y = 'Weight',
                hue = 'Algorithm', 
                style = 'Algorithm',
                markers = ["o", "X"], 
                palette = ['#FF5733', '#33C1FF'])

plt.xscale('log')
plt.yscale('log')

plt.title('Solution Weight by Algorithms (Log-Log Scale)')
plt.xlabel('Number of Vertices (log scale)')
plt.ylabel('Weight (log scale)')
plt.legend(title = 'Algorithm')

plt.show()