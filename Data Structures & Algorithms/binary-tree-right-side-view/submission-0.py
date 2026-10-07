# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        d = 0
        def rightside(node):
            if not node:
                return
            nonlocal d
            nonlocal ans
            ans.append(node.val)
            d += 1
            rightside(node.right)
        rightside(root)
        def trav(node, depth):
            nonlocal d
            nonlocal ans
            if not node:
                return
            if depth >= d:
                ans.append(node.val)
                d += 1
            trav(node.right, depth + 1)
            trav(node.left, depth + 1)
        trav(root, 0)
        return ans