class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        i = 0
        while i < len(intervals) - 1:
            cur1, cur2 = intervals[i][0], intervals[i][1]
            nex1, nex2 = intervals[i+1][0], intervals[i+1][1]
            if nex1 <= cur2 and nex2 >= cur2:
                intervals[i] = [cur1, nex2]
                intervals.pop(i+1)
                continue
            if nex1 >= cur1 and nex2 <= cur2:
                intervals.pop(i+1)
                continue
            i += 1
        return intervals


            