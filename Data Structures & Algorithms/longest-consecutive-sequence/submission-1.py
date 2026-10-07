class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            s.add(n)
        longest = 0
        for n in nums:
            if(n-1 not in s):
                cur = 1
                while(n+1 in s):
                    n += 1
                    cur += 1
                longest = max(cur, longest)
        return longest


