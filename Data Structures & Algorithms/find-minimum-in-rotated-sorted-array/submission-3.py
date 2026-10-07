class Solution:
    def findMin(self, nums: List[int]) -> int:
        hi, lo = len(nums)-1, 0
        ans = nums[0]

        while hi > lo:
            mid = lo + (hi - lo) // 2
            if(nums[mid] < nums[hi]):
                hi = mid
            else:
                lo = mid + 1
        return nums[lo]