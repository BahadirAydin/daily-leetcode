from .solution import Solution, TreeNode


def test_preorderTraversal():
    # Tree: [1, null, 2, 3]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    solution = Solution()
    assert solution.preorderTraversal(root) == [1, 2, 3]
