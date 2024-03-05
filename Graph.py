class Neighbour:
    def __init__(self, vertex_id, edge_weight):
        self.vertex_id = vertex_id
        self.edge_weight = edge_weight

    def __eq__(self, other):
        if self.vertex_id == other.vertex_id:
            return True
        else:
            return False


class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __eq__(self, other):
        if self.w == other.w:
            return True
        else:
            return False


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = []
        for i in range(num_vertices):
            self.graph.append([])

    def add_edge(self, src, dest, weight, undirected=True):
        neighbour = Neighbour(dest, weight)
        if neighbour not in self.graph[src]:
            self.graph[src].append(neighbour)
            if undirected:
                self.graph[dest].append(Neighbour(src, weight))
            return True
        else:
            # Debugging
            # print("Edge not added. Edge from {} to {} already exists".format(src, dest))
            return False

    def get_average_degree(self):
        sum_degrees = 0
        for v in self.graph:
            sum_degrees += len(v)
        return sum_degrees / self.num_vertices

    def print_graph(self):
        for i in range(self.num_vertices):
            print(" {} : ".format(i), end="")
            for ele in self.graph[i]:
                print(" -> {},{}".format(ele.vertex_id, ele.edge_weight), end="")
            print()

    def get_edges(self):
        edges = []
        for i in range(self.num_vertices):
            for ele in self.graph[i]:
                if i > ele.vertex_id: # Taking only one of the 2 entries per edge in list
                    edges.append(Edge(i, ele.vertex_id, ele.edge_weight))
        return edges

# if __name__ == "__main__":
#     num_vertices = 10
#
#     graph = Graph(num_vertices)
#     graph.add_edge(0, 1, 1)
#     graph.add_edge(0, 2, 1)
#     graph.add_edge(0, 3, 3)
#     graph.add_edge(0, 3, 1)
#     graph.add_edge(1, 2, 1)
#     graph.add_edge(2, 1, 1)
#
#     graph.print_graph()
