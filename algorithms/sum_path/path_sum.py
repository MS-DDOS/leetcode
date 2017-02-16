class tree_node(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def min_sum_path(node):
	if node == None:
		return 0

	path_sum = node.val
	if node.left == None:
		return node.val + min_sum_path(node.right)
	if node.right == None:
		return node.val + min_sum_path(node.left)

	return node.val + min(min_sum_path(node.right), min_sum_path(node.left))

tree = tree_node(10, tree_node(1), tree_node(4))
tree.left.left = tree_node(5)
tree.right.right = tree_node(1)

print min_sum_path(tree)