class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            # print(stack, ans)
            while stack and stack[-1][0] < t:
                j = stack.pop()[1]
                ans[j] = i-j
            stack.append((t, i))
        return ans

