import random

from Graph import Graph, Neighbour


def generate_graph(version, num_vertices):
    if version == 1:  # average vertex degree is 6
        return generate_6_degree_graph(num_vertices)
    elif version == 2:  # each vertex is adjacent to about 20% of the other vertices
        return generate_20_percent_graph(num_vertices)
    else:
        print("Version Incorrect")
        return None


def generate_6_degree_graph(num_vertices):
    if (num_vertices <= 6):
        print("ERROR!! Average degree can never reach 6!!")
        return None

    graph = Graph(num_vertices)
    graph = connected_cycle(graph)
    # Degree of each vertex is 2 now

    # Each edge contributes to a degree increment of 2. Adding 2*num_vertices edges will make average degree 6.
    for i in range(2 * num_vertices):
        src, dest, weight = generate_random_edge(num_vertices)
        while not graph.add_edge(src, dest, weight):  # if repeated edge, generate new edge
            src, dest, weight = generate_random_edge(num_vertices)

    if graph.get_average_degree() != 6:
        # To make up for repeated edges, just in case, but can never occur:
        print("This should not occur")
        while graph.get_average_degree() < 6:
            src, dest, weight = generate_random_edge(num_vertices)
            graph.add_edge(src, dest, weight)

    return graph


def generate_20_percent_graph(num_vertices):
    graph = Graph(num_vertices)
    graph = connected_cycle(graph)
    neighbour_count = [2] * num_vertices  # Each vertex is connected to 2 other vertices.
    vertices = list(range(num_vertices))
    limit = int(0.2 * num_vertices)
    while len(neighbour_count) > 0:
        src_ind = get_unsatisfying_vertex(graph, vertices, neighbour_count, limit)
        if src_ind is None:
            break
        while neighbour_count[src_ind] < limit:
            dest_ind = get_unsatisfying_vertex(graph, vertices, neighbour_count, limit, vertices[src_ind])
            if dest_ind is None:
                break
            if graph.add_edge(vertices[src_ind], vertices[dest_ind], random_weight()):
                neighbour_count[src_ind] += 1
                neighbour_count[dest_ind] += 1
                if neighbour_count[dest_ind] > limit:
                    neighbour_count.pop(dest_ind)
                    vertices.pop(dest_ind)
        neighbour_count.pop(src_ind)
        vertices.pop(src_ind)

    return graph


def connected_cycle(graph):
    vertices = list(range(graph.num_vertices))
    random.shuffle(vertices)
    for i in range(len(vertices) - 1):
        graph.add_edge(vertices[i], vertices[i + 1], random_weight())

    # Not necessary:
    graph.add_edge(vertices[len(vertices) - 1], vertices[0], random_weight())
    return graph


def random_weight():
    return random.randint(1, 100)


def generate_random_edge(num_vertices):
    while True:
        i = random.randint(0, num_vertices - 1)
        j = random.randint(0, num_vertices - 1)
        if i != j:
            return i, j, random_weight()


def get_desparate_edge(graph, vertices, neighbour_count, limit, src):
    if src is None:
        for i in range(len(neighbour_count)):
            if neighbour_count[i] < limit:
                return i
        return None
    else:
        for i in range(len(neighbour_count)):
            if vertices[i] is not src and neighbour_count[i] < limit:
                if Neighbour(vertices[i], 0) not in graph.graph[src]:
                    return i
        return None


def get_unsatisfying_vertex(graph, vertices, neighbour_count, limit, src=None):
    max_loop = 3
    i = 0
    num_vertices = len(neighbour_count)
    while num_vertices > 0:
        i += 1
        num_vertices = len(neighbour_count)
        if num_vertices == 0:
            return None
        j = random.randint(0, num_vertices - 1)
        if src != vertices[j] and neighbour_count[j] < limit:
            return j
        elif src is None and neighbour_count[j] >= limit:
            vertices.pop(j)
            neighbour_count.pop(j)

        if i > max_loop:
            return get_desparate_edge(graph, vertices, neighbour_count, limit, src)


# if __name__ == "__main__":
#     n = 5000
#     cg = generate_graph(2, n)
#     cnt = 0
#     edge_count = 0
#     for i in cg.graph:
#         if len(i) < int(0.2 * n):
#             print(len(i))
#             cnt += 1
#         edge_count += len(i)
#     if (cnt > 0):
#         print(str(cnt) + " vertices have less than 20% edges")
#
#     print("Edge Count : ", edge_count)
