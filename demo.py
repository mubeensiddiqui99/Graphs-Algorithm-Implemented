# import sys
from prims_algorithm import PrimsAlgorithm
# from kruskal_algorithm import KruskalAlgorithm
# from dijkstra_algorithm import DijkstraAlgorithm
# from Bellman_algorithm import BellmanAlgorithm
# from floyd_algorithm import FloydAlgorithm

from graph_builder import GraphBuilder
from graph_saver import GraphSaver
import networkx as nx


input_file = "input10.txt"
output_file = "graph"
highlight_color = 'green'
regular_color = 'blue'
node_color = 'yellow'
print("hi")
graph = GraphBuilder.build_graph_from_file(input_file)
pos = nx.spring_layout(graph)
prims = PrimsAlgorithm(graph)
# visited, path = DijkstraAlgorithm(graph)
#print(visited, path)
# kruskal = KruskalAlgorithm(graph, edges)
graph_saver = GraphSaver(output_file, highlight_color, regular_color, node_color)
initial_file = graph_saver.save_highlighted_tree(graph, pos, [])

output_files = [initial_file]
min_span_tree_generator = prims.min_span_tree_generator()
for tree in min_span_tree_generator:
        file = graph_saver.save_highlighted_tree(graph, pos, tree)
        output_files.append(file)

graph_saver.save_gif(output_files)
print("Min spanning tree: " + str(tree))

# output_files = [initial_file]
# min_span_tree_generator = kruskal
# for tree in min_span_tree_generator:
#         file = graph_saver.save_highlighted_tree(graph, pos, tree)
#         output_files.append(file)
#
# graph_saver.save_gif(output_files)
# print("Min spanning tree: " + str(tree))
