class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        start = [n, n]
        def solve(s, remain):
            if len(s) == n * 2:
                ans.append(s)
                return
            if remain[0] > 0:
                remain[0] -= 1
                solve(s + '(', remain)
                remain[0] += 1
            if remain[1] > remain[0]:
                remain[1] -= 1
                solve(s + ')', remain)
                remain[1] += 1
            return
        solve("", start)
        return ans