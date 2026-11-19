class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        p1, p2 = 0, 0
        ans = 0
        z = 0
        while p2 < len(nums):
            if nums[p2] == 0:
                z += 1
            while z > k:
                if nums[p1] == 0:
                    z -= 1
                p1 += 1
            ans = max(ans, p2-p1+1)
            p2 += 1
        return ans