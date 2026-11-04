# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {}

        for i in range(len(inorder)):
            inorder_index[inorder[i]] = i

        pre_i = 0

        def solve(left, right):
            nonlocal pre_i

            if left > right:
                return None

            root = TreeNode(preorder[pre_i])
            pre_i += 1

            i = inorder_index[root.val]

            root.left = solve(left, i - 1)
            root.right = solve(i + 1, right)

            return root

        return solve(0, len(inorder) - 1)