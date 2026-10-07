class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            s1 = heapq.heappop_max(stones)
            s2 = heapq.heappop_max(stones)
            if s1 == s2:
                continue
            else:
                heapq.heappush_max(stones, s1 - s2)
        if stones:
            return stones[0]
        return 0