class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                if not stack:
                    ans.append(a)
                    continue
                if stack[-1] > abs(a):
                    continue
                elif stack[-1] == abs(a):
                    stack.pop()
                else:
                    while stack and stack[-1] < abs(a):
                        stack.pop()
                    if not stack:
                        ans.append(a)
                    elif stack[-1] == abs(a):
                        stack.pop()
        return ans + stack