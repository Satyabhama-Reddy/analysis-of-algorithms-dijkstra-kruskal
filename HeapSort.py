# from Graph import Edge


def leftIndex(pos):
    return (2 * pos) + 1


def rightIndex(pos):
    return (2 * pos) + 2


def swap(edges, i, j):
    if i != j:
        edges[i], edges[j] = (edges[j], edges[i])


def heapify(edges, size, i):
    smallest = i
    l = leftIndex(i)
    r = rightIndex(i)

    if l < size and edges[smallest].w > edges[l].w:
        smallest = l

    if r < size and edges[smallest].w > edges[r].w:
        smallest = r

    if smallest != i:
        swap(edges, smallest, i)
        heapify(edges, size, smallest)


def heapSort(edges):
    size = len(edges)

    for i in range(size // 2 - 1, -1, -1):
        heapify(edges, size, i)

    for i in range(size - 1, 0, -1):
        swap(edges, i, 0)
        heapify(edges, i, 0)

# if __name__ == '__main__':
#
#     arr = [Edge(12,1,2), Edge(12,1,3), Edge(12,1,2), Edge(12,1,1)]
#
#     heapSort(arr)
#     N = len(arr)
#
#     for i in range(N):
#         print(arr[i].u, arr[i].v, arr[i].w)
