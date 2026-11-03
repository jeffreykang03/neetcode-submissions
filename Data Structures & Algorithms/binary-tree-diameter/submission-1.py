# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def solve(node):
            nonlocal ans
            if not node:
                return 0
            r, l = solve(node.right), solve(node.left)
            ans = max(ans, r + l)
            return 1 + max(r, l)
        solve(root)
        return ans
