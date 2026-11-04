# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solve(node, mini, maxi):
            if not node:
                return True
            if node.val <= mini or node.val >= maxi:
                return False
            return solve(node.left, mini, node.val) and solve(node.right, node.val, maxi)
        return solve(root, -1000000001, 1000000001)