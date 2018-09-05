class Node:
	def __init__(self, id, connected_to):
		self.id = id
		self.connected_to = connected_to
		self.visited = False

	def connect(self, id):
		if id in self.connected_to:
			raise ValueError("{} already connected".format(id))
		self.connected_to.append(id)

	def __str__(self):
		return "{}: {}".format(self.id, self.connected_to)

class NodeAndPath:
	def __init__(self, node, path):
		self.node = node
		self.path = path

def search_path_bfs(graph, start_id, end_id):
	if start_id not in graph:
		return None
	s = graph[start_id]
	q = [NodeAndPath(s, "")]
	paths = []
	while len(q) > 0:
		np = q.pop()
		n = np.node
		n.visited = True
		np.path = np.path + n.id
		if n.id == end_id:
			paths.append(np.path)
		for c in n.connected_to:
			cn = graph[c]
			if not cn.visited:
				q.insert(0, NodeAndPath(cn, np.path))
	return paths

if __name__=="__main__":
	a = Node("A", ["B"])
	b = Node("B", ["C", "E"])
	c = Node("C", ["A", "C", "D"])
	d = Node("D", [])
	e = Node("E", ["D"])
	# print(a, b, c, d, e)

	graph = {
		a.id: a,
		b.id: b,
		c.id: c,
		d.id: d,
		e.id: e,
	}
	path = search_path_bfs(graph, a.id, d.id)
	print(path)

