class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        p1 = 0
        zeros = 0
        best = 0

        for p2 in range(len(nums)):
            if nums[p2] == 0:
                zeros += 1

            while zeros > k:
                if nums[p1] == 0:
                    zeros -= 1
                p1 += 1

            best = max(best, p2 - p1 + 1)

        return best