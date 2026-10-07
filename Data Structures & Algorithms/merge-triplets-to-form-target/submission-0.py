class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = []
        for t in triplets:
            if t == target:
                return True
            flag = True
            for i in range(3):
                if t[i] > target[i]:
                    flag = False
            if flag:
                good.append(t)
        print(good)
        check = [0, 0, 0]
        for t in good:
            for i in range(3):
                if t[i] == target[i]:
                    check[i] = 1
        print(check)
        return check == [1, 1, 1]
        
