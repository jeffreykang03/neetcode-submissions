class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        ans = 0

        def dfs(x, y):
            if (x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] == 0):
                return 0
            grid[x][y] = 0
            i = 0
            for (dirx, diry) in dirs:
                i += dfs(x + dirx, y + diry)
            return 1 + i
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 1):
                    ans = max(ans, dfs(i, j))
        return ans