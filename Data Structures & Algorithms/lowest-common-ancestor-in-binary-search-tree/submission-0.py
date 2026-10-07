# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        l = min(p.val, q.val)
        r = max(p.val, q.val)
        def solve(node):
            if l <= node.val <= r:
                return node
            if node.val > r:
                return solve(node.left)
            return solve(node.right)
        return solve(root)