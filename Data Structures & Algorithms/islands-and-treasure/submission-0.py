class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        from collections import deque
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    for d in dirs:
                        if 0 <= i + d[0] < len(grid) and 0 <= j + d[1] < len(grid[0]) and grid[i + d[0]][j + d[1]] > 1:
                            grid[i+d[0]][j+d[1]] = 1
                            q.append((i+d[0], j+d[1], 1))
        
        while q:
            x, y, step = q.popleft()
            step += 1
            for d in dirs:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] > step:
                    grid[nx][ny] = step
                    q.append((nx, ny, step))