
class Edge:
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def __str__(self):
		print("{} -> {}".format(self.start, self.end))

class Node:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		print(self.name)

class DirectedGraph:
	def __init__(self, nodes, edges):
		self.nodes = nodes
		self.edges = edges

def find_route(start, end, path, graph):
	for e in graph.edges:
		if e.start.name is start.name:
			# we found a starting edge
			# check if the end node 
			if 

if __name__ == "__main__":
