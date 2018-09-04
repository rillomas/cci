import random

class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __str__(self):
		if self.left and not self.right:
			return "[{} {}]".format(self.val, self.left)
		elif self.right and not self.left:
			return "[{} {}]".format(self.val, self.right)
		elif not self.left and not self.right:
			return "[{}]".format(self.val)
		else:
			return "[{} {} {}]".format(self.val, self.left, self.right)

def gen_bst(arr):
	arr_len = len(arr)
	if arr_len == 0:
		return None
	elif arr_len == 1:
		return Node(arr[0])
	elif arr_len == 2:
		# left is always smaller
		return Node(arr[1], arr[0])
	elif arr_len == 3:
		# left is smaller, right is bigger
		return Node(arr[1], arr[0], arr[2])
	else:
		# take the center, start, end and make a subtree
		center = arr_len // 2
		lt = arr[:center]
		rt = arr[center+1:]
		# print(center)
		# print("left: ", lt)
		# print("right: ", rt)
		return Node(arr[center],
			        gen_bst(lt),
			        gen_bst(rt))

if __name__ == "__main__":
	random.seed(12345)
	arr = [random.randint(0, 100) for _ in range(8)]
	sorted_arr = sorted(arr)
	print("input: ", sorted_arr)
	bst = gen_bst(sorted_arr)
	print("output: ",bst)
	#root = Node(1)
	#sprint(root)
