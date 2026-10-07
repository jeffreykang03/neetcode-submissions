# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        q = deque()
        q.append([root, 0])
        ans = []
        level = 0
        while q:
            cur, curlev = q.popleft()
            while len(ans) - 1 < curlev:
                ans.append([])
            ans[curlev].append(cur.val)
            if cur.left:
                q.append([cur.left, curlev + 1])
            if cur.right:
                q.append([cur.right, curlev + 1])
        return ans

