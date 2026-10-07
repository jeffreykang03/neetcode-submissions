class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9':'wxyz'}
        if not digits:
            return ans
        def solve(cur, pos):
            if pos >= len(digits)-1:
                for l in letters[digits[pos]]:
                    ans.append(cur + l)
                return
            for l in letters[digits[pos]]:
                solve(cur + l, pos + 1)
        solve("", 0)
        return ans