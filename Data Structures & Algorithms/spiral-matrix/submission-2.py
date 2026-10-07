class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        mark = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        dire = {'n': [-1, 0], 'w': [0, 1], 's': [1, 0], 'e': [0, -1]}
        cur = 'w'
        x, y = 0, 0
        while len(ans) <= len(matrix) * len(matrix[0]):
            while 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and mark[x][y] == 0:
                print('add', (x, y))
                ans.append(matrix[x][y])
                mark[x][y] = 1
                x += dire[cur][0]
                y += dire[cur][1]
            print(x, y, cur)
            print(ans)
            if cur == 'w':
                cur = 's'
                y -= 1
                x += 1
            elif cur == 's':
                cur = 'e'
                x -= 1
                y -= 1
            elif cur == 'e':
                cur = 'n'
                y += 1
                x -= 1
            elif cur == 'n':
                cur = 'w'
                x += 1
                y += 1
            if len(ans) == len(matrix) * len(matrix[0]):
                break
        return ans
