class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        start, ind = 0, 1
        ans = 0
        while start < len(points):
            i1 = points[start]
            while ind < len(points) and points[ind][0] <= i1[1]:
                ind += 1
            # print(i1, ind, ans)
            start = ind
            ind += 1
            ans += 1
        return ans
