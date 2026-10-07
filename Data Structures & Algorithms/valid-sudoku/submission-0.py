class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if(len(board) != 9):
            return False
        for i in range(9):
            if(len(board[i]) != 9):
                return False
        for r in board:
            req = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
            for ch in r:
                if(ch != '.'):
                    if(int(ch) not in req):
                        return False
                    req.remove(int(ch))
        
        for i in range(9):
            req = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
            for j in range(9):
                ch = board[j][i]
                if(ch != '.'):
                    if(int(ch) not in req):
                        return False
                    req.remove(int(ch))
        for x in [0, 3, 6]:
            for y in [0, 3, 6]:
                req = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
                xm = [0, 1, 2]
                ym = [0, 1, 2]
                for i in xm:
                    for j in ym:
                        ch = board[x+i][y+j]
                        if(ch != '.'):
                            if(int(ch) not in req):
                                return False
                            req.remove(int(ch))
        return True