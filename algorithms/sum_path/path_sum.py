class tree_node(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def min_sum_path(node):
	if node == None:
		return None

	path_sum = node.val
	left_sum = min_sum_path(node.left)
	right_sum = min_sum_path(node.right)

	if left_sum == None and right_sum == None:
		return path_sum
	elif right_sum == None:
		path_sum += left_sum
	elif left_sum == None:
		path_sum += right_sum
	else:
		if(left_sum <= right_sum):
			path_sum += left_sum
		else:
			path_sum += right_sum

	return path_sum

tree = tree_node(10, tree_node(1), tree_node(4))
tree.left.left = tree_node(5)
tree.right.right = tree_node(1)

print min_sum_path(tree)