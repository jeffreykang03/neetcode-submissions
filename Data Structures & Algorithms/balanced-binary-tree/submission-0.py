# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def solve(node):
            nonlocal ans
            if not node:
                return 0
            r = solve(node.right)
            l = solve(node.left)
            if abs(r-l) > 1:
                ans = False
            return max(r, l) + 1
        solve(root)
        return ans