class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 1
        ans = 1
        cur = set()
        cur.add(s[0])
        while r < len(s):
            if s[r] in cur:
                # print(l, r, ans)
                ans = max(ans, r-l)
                while s[l] != s[r]:
                    cur.remove(s[l])
                    l += 1
                l += 1
                # print(l, ans)
            cur.add(s[r])
            r += 1
        # print(l, r)
        ans = max(ans, r-l)
        return ans