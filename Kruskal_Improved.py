from Graph import Graph

def leftIndex(pos):
	return (2 * pos) + 1

def rightIndex(pos):
	return (2 * pos) + 2

def swap(edges, i, j):
	if i != j:
		edges[i], edges[j] = (edges[j], edges[i])

def heapify(edges, size, i):
	largest = i
	l = leftIndex(i)
	r = rightIndex(i)

	if l < size and edges[largest].w < edges[l].w:
		largest = l

	if r < size and edges[largest].w < edges[r].w:
		largest = r

	if largest != i:
		swap(edges, largest, i)
		heapify(edges, size, largest)


def buildHeap(edges):
	size = len(edges)

	for i in range(size // 2 - 1, -1, -1):
		heapify(edges, size, i)


def popMax(arr, n):
	if n == 0:
		return None
	max_ele = arr[0]
	lastElement = arr[n - 1]
	arr[0] = lastElement
	heapify(arr, n - 1, 0)
	return max_ele


class Kruskal_Improved:

	def __init__(self):
		# Make set
		self.T = None
		self.dad = []
		self.rank = []

	def makeSet(self):
		self.dad.append(-1)
		self.rank.append(0)

	def union(self, r1, r2):
		# merge 2 sets r1 and r2 into a single set
		if self.rank[r1] > self.rank[r2]:
			self.dad[r2] = r1
		elif self.rank[r1] < self.rank[r2]:
			self.dad[r1] = r2
		else:
			self.dad[r1] = r2
			self.rank[r2] += 1

	def find(self, v):
		# Find the set containing v
		r = v
		s = []
		while self.dad[r] != -1:
			s.append(r)
			r = self.dad[r]
		while s:
			self.dad[s.pop()] = r
		return r

	def Kruskal_MST(self, G):
		edges = G.get_edges()
		buildHeap(edges) # CHANGED
		for i in range(G.num_vertices):
			self.makeSet()  # appending

		self.T = Graph(G.num_vertices)
		edge_count = 0
		n_heap = len(edges)
		while True:
			e = popMax(edges, n_heap)  # CHANGED
			if e is None:
				break
			n_heap -= 1
			ru = self.find(e.u)
			rv = self.find(e.v)
			if ru != rv:
				self.T.add_edge(e.u, e.v, e.w)
				self.union(ru, rv)
				edge_count += 1
				if edge_count == G.num_vertices - 1:
					break
		return self.T

	def Kruskal_BW(self, G, s, t):
		MST = self.Kruskal_MST(G)
		color = [0] * G.num_vertices
		bw = 100000  # MAX

		path = self.DFS(MST, color, s, t, [])
		for i in range(len(path)-1):
			for edge in G.graph[path[i]]:
				if edge.vertex_id == path[i + 1]:
					bw = min(bw, edge.edge_weight)
		return path, bw

	def DFS(self, G, color, s, t, path):
		color[s] = 1
		path.append(s)
		if s == t:
			return path
		for e in G.graph[s]:
			if color[e.vertex_id] == 0:
				if self.DFS(G, color, e.vertex_id, t, path):
					return path
		path.pop()

