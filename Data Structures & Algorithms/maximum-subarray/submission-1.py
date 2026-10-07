class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = []
        pre.append(nums[0])
        for i in nums[1:]:
            pre.append(pre[-1] + i)
        print(pre)
        hi = 1
        ans = pre[0]
        mini = min(0, pre[0])
        while hi < len(pre):
            print(hi)
            while(hi != len(pre) - 1 and pre[hi] < pre[hi + 1]):
                mini = min(mini, pre[hi])
                hi = hi + 1
            print(hi, pre[hi], mini)
            ans = max(ans, pre[hi] - mini)
            mini = min(mini, pre[hi])
            hi = hi + 1
            
        return ans

            