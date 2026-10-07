class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        ans = -1
        mark = set()
        mHep = [(0, k)]
        while mHep:
            w1, n1 = heapq.heappop(mHep)
            if n1 in mark:
                continue
            mark.add(n1)
            ans = w1

            for n2, w2 in adj[n1]:
                if n2 not in mark:
                    heapq.heappush(mHep, (w1 + w2, n2))
        return ans if len(mark) == n else -1

