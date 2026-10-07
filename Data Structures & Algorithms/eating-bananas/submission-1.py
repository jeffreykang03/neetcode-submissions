class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # int ans = sum(piles) / 
        hi = max(piles)
        lo = 1
        mid = 0
        while hi >= lo:
            mid = lo + ((hi - lo) // 2)
            hrs = 0
            for p in piles:
                hrs = hrs + p // mid + (p % mid != 0)
            print(hrs, lo, mid, hi)
            if hrs > h:
                lo = mid + 1
            else:
                ans = mid
                hi = mid - 1
        return ans

