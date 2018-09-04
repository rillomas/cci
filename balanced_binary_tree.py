
class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def is_leaf(self):
		return self.left is None and self.right is None

	def __str__(self):
		if self.is_leaf():
			return "[{}]".format(str(self.value))
		else:
			return "[{}, {}, {}]".format(str(self.value),
										 str(self.left),
										 str(self.right))

def get_height(node):
	if node is None:
		return 0
	left = get_height(node.left)
	right = get_height(node.right)
	return 1 + max(left, right)


def print_tree(root):
	print(root.left)
	print(root.right)
	print(root.value)

def is_balanced(root):
	if root is None:
		return True
	# get height for left tree
	left_height = get_height(root.left)
	# get height for right tree
	right_height = get_height(root.right)
	diff = abs(left_height - right_height)
	if diff >= 2:
		return False
	else:
		lb = is_balanced(root.left)
		rb = is_balanced(root.right)
		return lb and rb


if __name__ == "__main__":
	n = Node(1,
			 Node(2, Node(3), Node(4)),
			 Node(5, Node(6), Node(7, Node(8, Node(9)))))
	#print_tree(n)
	print(n)
	print(get_height(n))
	print(is_balanced(n))
