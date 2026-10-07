class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return x**2 + y**2
        hep = []
        for p in points:
            heapq.heappush(hep, (dist(p[0], p[1]), p))
        ans = []
        for i in range(k):
            ans.append(hep[0][1])
            heapq.heappop(hep)
        return ans
