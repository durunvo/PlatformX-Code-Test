
class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

# This function give O(n) because it needs to go through each node. Time will increase linear with number of nodes.
def find_lca(root, n1, n2):

	if root is None:
		return None

	if root.value == n1 or root.value == n2:
		return root

	left = find_lca(root.left, n1, n2)
	right = find_lca(root.right, n1, n2)

	if left and right:
		return root

	return left if left is not None else right

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print find_lca(root, 6, 7).value
    print find_lca(root, 3, 7).value

if __name__ == "__main__":
    main()
