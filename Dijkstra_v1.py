"""
status:
    -1 : unseen
    0 : fringer
    1 : intree
"""


def getLargestFringer(status, b_width):
    max_value = -1
    max_fringer = -1
    for i in range(len(status)):
        if status[i] == 0 and max_value < b_width[i]:
            max_value = b_width[i]
            max_fringer = i
    return max_fringer


def Dijkstra_BW_v1(G, s, t):
    status = []
    b_width = []
    dad = []

    for v in range(G.num_vertices):
        status.append(-1)
        b_width.append(0)
        dad.append(0)

    status[s] = 1
    b_width[s] = 100000  # MAX
    dad[s] = -1

    for e in G.graph[s]:
        status[e.vertex_id] = 0
        b_width[e.vertex_id] = e.edge_weight
        dad[e.vertex_id] = s

    v = getLargestFringer(status, b_width)
    while v != -1:
        status[v] = 1
        for w in G.graph[v]:
            min_bw = min(b_width[v], w.edge_weight)
            if status[w.vertex_id] == -1:
                status[w.vertex_id] = 0
                b_width[w.vertex_id] = min_bw
                dad[w.vertex_id] = v
            elif status[w.vertex_id] == 0 and b_width[w.vertex_id] < min_bw:
                b_width[w.vertex_id] = min_bw
                dad[w.vertex_id] = v

        v = getLargestFringer(status, b_width)

    path = []
    cur = t
    while cur != -1: # connected graph, hence path must exist
        path.append(cur)
        cur = dad[cur]

    for i in range(int(len(path)/2)):
        temp = path[i]
        path[i] = path[-(i+1)]
        path[-(i+1)] = temp

    return path, b_width[t]




