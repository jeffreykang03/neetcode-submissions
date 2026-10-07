class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cur = defaultdict(int)
        target = defaultdict(int)
        if len(s1) > len(s2):
            return False
        p1 = 0
        p2 = len(s1)
        for i in range(len(s1)):
            cur[s2[i]] += 1
        for c in s1:
            target[c] += 1
        while p2 <= len(s2):
            if cur == target:
                print(p1, p2-1)
                print(cur, target)
                return True
            cur[s2[p1]] -= 1
            if cur[s2[p1]] <= 0:
                cur.pop(s2[p1])
            if p2 < len(s2):
                cur[s2[p2]] += 1
            p1 += 1
            p2 += 1
        return False
