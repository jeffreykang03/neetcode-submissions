class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1
        while p2 > p1:
            while(not(s[p1] in "1234567890qwertyuiopasdfghjklzxcvbnmABCDEFGHIJKLMNOPQRSTUVWXYZ") and p1 < p2):
                p1 = p1 + 1
            while(not(s[p2] in "1234567890qwertyuiopasdfghjklzxcvbnmABCDEFGHIJKLMNOPQRSTUVWXYZ") and p1 < p2):
                p2 = p2 - 1
            if(p1 == p2):
                return True
            if(s[p1].upper() != s[p2].upper()):
                return False
            p2 = p2 - 1
            p1 = p1 + 1

        return True