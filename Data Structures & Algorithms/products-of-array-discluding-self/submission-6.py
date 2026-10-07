class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tot = 1
        zcount = 0
        for i in nums:
            if(i != 0):
                tot = tot * i
            else:
                if(zcount == 1):
                    lose = []
                    for i in nums:
                        lose.append(0)
                    return lose
                zcount += 1
        out = []
        for i in nums:
            if(i == 0):
                out.append(int(tot))
            else:
                if(zcount == 1):
                    out.append(0)
                else:
                    out.append(int(tot / i))
        return out
        