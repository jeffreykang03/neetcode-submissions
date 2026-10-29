class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] >= len(nums)-1:
            return 1
        cur = 0
        ans = 0
        while cur < len(nums):
            stride = nums[cur]
            best = cur + nums[cur]
            nextind = cur + 1

            for i in range(1, stride+1):
                scout = cur + nums[cur + i] + i
                print(scout, cur, i, "bruh")
                if scout >= len(nums) - 1:
                    print(cur, scout, ans)
                    return ans + 2
                if scout > best:
                    best = scout
                    nextind = cur + i
            ans += 1
            print(cur, nextind, best, ans)
            cur = nextind
            
        return -1
                
