# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ans = root
        def dfs(node):
            nonlocal ans
            if not node:
                return False
            print(node.val)
            l = dfs(node.left)
            r = dfs(node.right)
            print('A', l, r, node.val)
            if l and r and ans == root:
                print('AA', node.val)
                ans = node
            if node == p or node == q:
                print('AAA', node.val)
                if l or r:
                    print('AAAA', node.val)
                    ans = node
                return True
            if l or r:
                print('B', node.val)
                return True
            return False
        dfs(root)
        return ans