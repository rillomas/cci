class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.val)

def traverse_bfs(node):
	if node is None:
		return
	q = [node]
	while len(q) > 0:
		n = q.pop()
		print(n.val)
		if n.left:
			q.insert(0, n.left)
		if n.right:
			q.insert(0, n.right)

def traverse_dfs(node):
	if node is None:
		return
	print(node.val)
	if node.left:
		traverse_dfs(node.left)
	if node.right:
		traverse_dfs(node.right)

if __name__=="__main__":
	tree = Node(1,
				Node(2, Node(3),Node(4)),
				Node(5, Node(6),Node(7)))
	#print(tree)
	traverse_bfs(tree)
	traverse_dfs(tree)

