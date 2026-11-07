class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        ans = {}
        visited = set()
        for t in times:
            adj[t[0]].append((t[1], t[2]))
        # print(adj)
        import heapq
        pq = []
        heapq.heappush(pq, (0, k))
        while pq:
            t, u = heapq.heappop(pq)
            if u in visited:
                continue
            ans[u] = t
            visited.add(u)
            
            for pair in adj[u]:
                if pair[0] not in visited:
                    heapq.heappush(pq, (pair[1] + t, pair[0]))
        # print(ans)
        return max(ans.values()) if len(ans) == n else -1