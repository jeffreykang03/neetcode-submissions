class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        hi, lo = sum(weights), max(weights)
        mid = 0
        ans = hi
        while hi >= lo:
            mid = lo + (hi - lo) // 2
            cur, ships = 0, 1
            for w in weights:
                if cur + w > mid:
                    cur = 0
                    ships += 1
                cur += w
            if ships > days:
                lo = mid + 1
            else:
                ans = mid
                hi = mid - 1
        return ans