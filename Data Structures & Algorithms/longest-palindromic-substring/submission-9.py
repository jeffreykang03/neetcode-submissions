class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = 1
        ans = ""
        for i in range(len(s)):
            k = 1
            cur = s[i]
            while i + k < len(s) and k <= i:
                l, r = s[i-k], s[i+k]
                if l != r:
                    if len(cur) > best:
                        best = len(cur)
                        ans = cur
                    break
                k += 1
                cur = l + cur + r
            if len(cur) > len(ans):
                ans = cur
                best = len(cur)
            j = i + 1
            k = i
            cur = ""
            while k >= 0 and j < len(s):
                l, r = s[k], s[j]
                if l != r:
                    if len(cur) > best:
                        best = len(cur)
                        ans = cur
                    break
                k -= 1
                j += 1
                cur = l + cur + r
            # if i == 2:
            #     return cur
            if len(cur) > len(ans):
                ans = cur
                best = len(cur)
        return ans

