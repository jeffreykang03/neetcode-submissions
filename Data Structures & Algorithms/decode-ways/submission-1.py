class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 4)
        if s[0] == '0':
            return 0
        dp[0] = 1
        for i in range(len(s)):
            if s[i] == '1':
                dp[i+2] += dp[i]
            elif s[i] == '2' and i < len(s)-1 and int(s[i+1]) < 7:
                dp[i+2] += dp[i]
            if s[i] != '0':
                dp[i+1] += dp[i]
        print(dp)
        return dp[len(s)]