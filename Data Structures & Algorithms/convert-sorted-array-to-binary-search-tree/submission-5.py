class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def solve(arr):
            if not arr:
                return None
            # if len(arr) == 1:
            #     return TreeNode(val=arr[0])
            out = TreeNode()
            mid = len(arr) // 2
            out.val = arr[mid]
            out.left = solve(arr[:mid])
            out.right = solve(arr[mid+1:])
            return out
        nums.sort()
        return solve(nums)