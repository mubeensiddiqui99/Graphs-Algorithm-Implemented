class KruskalAlgorithm:
    """ Used to create minimum spanning tree of a graph
    """

    parent = dict()
    rank = dict()

    def make_set(vertice):
        parent[vertice] = vertice
        rank[vertice] = 0

    def find(vertice):
        if parent[vertice] != vertice:
            parent[vertice] = find(parent[vertice])
        return parent[vertice]

    def union(vertice1, vertice2):
        root1 = find(vertice1)
        root2 = find(vertice2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
        else:
            parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

    def __init__(self, graph):
        self.graph = graph

    def min_span_tree_generator(self, edges):
        """ Generator that runs the steps in Prim's algorithm

        :yield: Eventually a list of all edges that makes up the minimum spanning tree
        """
        graph = self.graph
        total_cost = 0
        for node in graph.nodes(data='name'):
            make_set(node)
            minimum_spanning_tree = set()
            edges.sort()
        for edge in edges:
            weight, node1, node2 = edge
            if find(node1) != find(node2):
                union(node1, node2)
                minimum_spanning_tree.add(edge)
            print(total_cost)
