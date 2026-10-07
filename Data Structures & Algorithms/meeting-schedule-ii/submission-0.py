"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        time = []
        for i in intervals:
            time.append((i.start, 1))
            time.append((i.end, -1))

        time.sort(key=lambda x: (x[0], x[1]))

        res = count = 0
        for t in time:
            count += t[1]
            res = max(res, count)
        return res

        # intervals.sort(key = lambda x: x[1])
        
        # ans = 0
        # i = 0
        # n = len(intervals)
        # while(i < n):
        #     j = i + 1
        #     # flag = False
        #     while(j < n and intervals[i][1] < intervals[j][0]):
        #         j = j + 1
        #         # if intervals[i][1] >= intervals[j][0]:
        #         #     flag = True
        #     i = j
        #     while(j < n and intervals[j][0] < intervals[i][1]):
        #         j = j + 1
        #     # if(flag):
        #     #     ans = ans + 1
        # return ans - 1
