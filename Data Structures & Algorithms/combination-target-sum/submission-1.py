class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def solve(i, cur, total):
            if total == target:
                ans.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            cur.append(nums[i])
            solve(i, cur, total + nums[i])
            cur.pop()
            solve(i + 1, cur, total)
        solve(0, [], 0)
        return ans