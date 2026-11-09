class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        dist = [[float('inf')] * (k + 5) for _ in range(n)]
        for f, t, p in flights:
            adj[f].append((p, t))

        import heapq
        heap = []
        heapq.heappush(heap, (0, src, -1))
        while heap:
            pri, node, stops = heapq.heappop(heap)
            if dst == node: return pri
            if stops == k or pri > dist[node][stops + 1]:
                continue
            for w, nei in adj[node]:
                newpri = pri + w
                newstops = stops + 1
                if newpri < dist[nei][newstops + 1]:
                    dist[nei][newstops + 1] = newpri
                    heapq.heappush(heap, (newpri, nei, newstops))
        return -1
