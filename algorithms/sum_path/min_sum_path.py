class tree_node(object):
	def __init__(self, value=0, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def min_sum_path(node):
	if node == None:
		return 0

	path_sum = node.value;
	left_sum = min_sum_path(node.left)
	right_sum = min_sum_path(node.right)

	if(left_sum <= right_sum):
		path_sum += left_sum
	else:
		path_sum += right_sum

	return path_sum

tree = tree_node(15)
tree.left = tree_node(10)
tree.left.left = tree_node(6)
tree.left.right = tree_node(7)
tree.left.right.left = tree_node(2)
tree.left.right.left.left = tree_node(0)
tree.left.right.left.right = tree_node(5)
tree.left.right.right = tree_node(16)
tree.left.right.right.left = tree_node(3)
tree.right = tree_node(20)
tree.right.left = tree_node(22)
print min_sum_path(tree)