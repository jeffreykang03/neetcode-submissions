class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def verify(x, y, i):
            dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            if i == len(word):
                return True
            saved = board[x][y]
            board[x][y] = '!'
            for d in dir:
                x1 = x + d[0]
                y1 = y + d[1]
                if 0 <= x1 < len(board) and 0 <= y1 < len(board[0]) and board[x1][y1] == word[i]:
                    print(x1, y1, board[x1][y1], word[i])
                    if verify(x1, y1, i+1):
                        return True
            board[x][y] = saved
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    print("start", i, j, word[0])
                    if verify(i, j, 1):
                        return True
        return False