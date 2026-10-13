class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0
        stack = []

        i = 0
        while i < n:
            start = i

            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                ans = max(ans, height * (i - index))
                start = index

            stack.append((start, heights[i]))
            i += 1
        while stack:
            index, height = stack.pop()
            ans = max(ans, height * (n - index))
        return ans                
