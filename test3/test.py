from main import find_lca, Node

def test():
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    assert find_lca(root1, 1, 1).value == 1
    assert find_lca(root1, 2, 1).value == 1
    assert find_lca(root1, 3, 1).value == 1
    assert find_lca(root1, 3, 2).value == 1
    assert find_lca(root1, 3, 3).value == 3
    root2 = Node(1)
    root2.left = Node(2)
    assert find_lca(root1, 1, 1).value == 1
    assert find_lca(root1, 2, 1).value == 1
    assert find_lca(root1, 3, 1).value == 1
    root3 = Node(1)
    root3.left = Node(2)
    root3.right = Node(3)
    root3.left.left = Node(4)
    root3.left.right = Node(5)
    root3.right.left = Node(6)
    root3.right.right = Node(7)
    assert find_lca(root3, 6, 7).value == 3
    assert find_lca(root3, 3, 7).value == 3
    assert find_lca(root3, 4, 5).value == 2
    assert find_lca(root3, 4, 6).value == 1
    assert find_lca(root3, 2, 4).value == 2

if __name__ == "__main__":
    test()
    print('Pass all test')
