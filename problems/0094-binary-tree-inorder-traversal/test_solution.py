from .solution import Solution, TreeNode


def test_inorderTraversal():
    # Tree: [1, null, 2, 3]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    solution = Solution()
    assert solution.inorderTraversal(root) == [1, 3, 2]
