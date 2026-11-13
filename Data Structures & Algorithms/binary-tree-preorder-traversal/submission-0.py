# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def preorder(node):
            if not node:
                return
            ans.append(node.val)
            left = preorder(node.left)
            right = preorder(node.right)
            if preorder(left):
                ans.append(left)
            if preorder(right):
                ans.append(right)
            return
        preorder(root)
        return ans