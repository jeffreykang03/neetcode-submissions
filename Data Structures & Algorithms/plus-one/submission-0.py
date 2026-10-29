class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        p = len(digits) - 1
        while digits[p] == 9:
            digits[p] = 0
            p -= 1
            if p < 0:
                digits = [1] + digits
        if p >= 0:
            digits[p] += 1
        return digits