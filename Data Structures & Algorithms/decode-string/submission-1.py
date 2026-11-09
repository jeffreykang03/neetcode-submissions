class Solution:
    def decodeString(self, s: str) -> str:
        def solve(i):
            ans = ""
            while i < len(s):
                if s[i] in "1234567890":
                    n = 0
                    while s[i] in "1234567890":
                        n *= 10
                        n += int(s[i])
                        i += 1
                    news, newi = solve(i+1)
                    ans += news*n
                    i = newi
                else:
                    if s[i] == ']':
                        # i += 1
                        break
                    ans += s[i]
                i += 1
            print(ans, i)
            return ans, i
        return solve(0)[0]
