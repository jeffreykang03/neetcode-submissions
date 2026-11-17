class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def solve(rem, cur):
            nonlocal ans
            if not rem:
                ans.append(cur.copy())
                # print(ans)
                return
            for i in range(len(rem)):
                cur.append(rem[i])
                # print(cur, 'a')
                solve(rem[:i] + rem[i+1:], cur)
                cur.pop()
                # print(cur, 'b')
            return
        solve(nums, [])
        return ans
