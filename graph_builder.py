import networkx as nx


class GraphBuilder:
    """ Helper class for working with networkx graphs
    """

    @staticmethod
    def build_graph_from_file(filename):
        """ Creates a graph from a given JSON file

        :param filename: The JSON source file of the graph
        :return: A networkx graph made from the given file
        """
        print("hiii")
        graph = nx.Graph()
        f = open(filename, 'r')
        x = f.seek(10)
        w = [int(x) for x in next(f).split()]
        w = w[0]
        print(w)
        inputnodes = []
        edges = []

        x = f.seek(14 + len(str(w)))

        for i in range(w):
            index, x, y = [float(x) for x in next(f).split()]
            inputnodes.append([int(x * 1300) + 25, int(y * 1000) + 50])
        x = f.read(1)
        for i in range(w):

            vertex = f.read(1)
            f.read(1)
            x = next(f).split('\t')
            graph.add_node(vertex)
            for i in range(int(len(x) / 4)):
                if x[i * 4] == '':
                    del x[i * 4]
                arr = [int(vertex), int(x[i * 4]), int(float(x[i * 4 + 2]) / 1000000)]
                graph.add_edge(arr[0], arr[1], weight=arr[2])
                edges.append(arr)
        return graph
