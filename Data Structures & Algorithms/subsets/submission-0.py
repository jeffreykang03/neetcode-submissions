class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subs = []
        def dfs(i):
            if i == len(nums):
                ans.append(subs.copy())
                return
            subs.append(nums[i])
            dfs(i+1)
            subs.pop()
            dfs(i+1)
        dfs(0)
        return ans