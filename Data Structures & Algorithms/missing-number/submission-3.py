class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mark = [False for i in range(len(nums) + 1)]
        for n in nums:
            mark[n] = True
        for i in range(len(mark)):
            if not mark[i]:
                return i
