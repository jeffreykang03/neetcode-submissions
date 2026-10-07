class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}
        for i, n in enumerate(nums):
            x[n] = i
        for i, n in enumerate(nums):
            if(target - nums[i] in x.keys() and i != x[target-nums[i]]):
                return [i, x[target-nums[i]]]