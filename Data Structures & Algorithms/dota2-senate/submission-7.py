class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        nex = ""
        while senate and 'R' in senate and 'D' in senate:
            nex = ""
            df, rf = 0, 0
            for ch in senate:
                if ch == 'R':
                    if rf >= 0:
                        df -= 1
                        nex += 'R'
                    else:
                        rf += 1
                else:
                    if df >= 0:
                        rf -= 1
                        nex += 'D'
                    else:
                        df += 1
            nex = nex.replace('D', '', -df)
            nex = nex.replace('R', '', -rf)
            senate = nex
            print(senate, df, rf)
        if 'R' in senate:
            return 'Radiant'
        else:
            return 'Dire'
