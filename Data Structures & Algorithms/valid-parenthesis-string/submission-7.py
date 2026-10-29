class Solution:
    def checkValidString(self, s: str) -> bool:
        omin = 0
        omax = 0
        for char in s:
            if char == '(':
                star = 0
                omin += 1
                omax += 1
            if char == ')':
                omin -= 1
                omax -= 1
            if char == '*':
                omin -= 1
                omax += 1
            if omin < 0:
                omin = 0
            if omax < 0:
                return False
        return omin == 0
        