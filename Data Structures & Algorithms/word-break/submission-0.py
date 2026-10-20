class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        wordDict = set(wordDict)
        def solve(i):
            if i == len(s) or (i in memo.keys() and memo[i] == True):
                return True
            if (i in memo.keys() and memo[i] == False):
                return False
            for w in wordDict:
                if ((i + len(w)) <= len(s) and
                     s[i : i + len(w)] == w
                ):
                    if solve(i + len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False

        return solve(0)