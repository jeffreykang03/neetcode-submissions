class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        import heapq
        pq = []
        visited = set()
        heapq.heappush(pq, (grid[0][0], 0, 0))
        visited.add((0, 0))
        while pq:
            val, x, y = heapq.heappop(pq)
            # print(val, x, y)
            if x == len(grid) - 1 and y == len(grid) - 1:
                return val
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for d in dirs:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    heapq.heappush(pq, (max(grid[nx][ny], val), nx, ny))
        return -1