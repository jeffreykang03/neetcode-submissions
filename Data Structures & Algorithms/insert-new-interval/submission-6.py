class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        used = False
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            used = True
        if newInterval[1] >= intervals[0][0] and newInterval[0] <= intervals[0][0]:
            intervals[0] = [newInterval[0], intervals[0][1]]
            used = True
        if newInterval[1] >= intervals[0][1] and newInterval[0] <= intervals[0][1]:
            intervals[0] = [intervals[0][0], newInterval[1]]
            used = True
        if newInterval[1] <= intervals[0][1] and newInterval[0] >= intervals[0][0]:
            used = True
        specint1, specint2 = newInterval[0], newInterval[1]
        i = 0
        while i < len(intervals) - 1:
            cur1, cur2 = intervals[i][0], intervals[i][1]
            nex1, nex2 = intervals[i+1][0], intervals[i+1][1]
            if not used and specint1 <= cur2 and specint2 >= cur2:
                intervals[i] = [cur1, specint2]
                used = True
                continue
            if not used and specint1 >= cur1 and specint2 <= cur2:
                used = True
                continue
            if not used and specint1 > cur2 and specint2 < nex1:
                intervals.insert(i+1, newInterval)
                used = True
                continue
            if nex1 <= cur2 and nex2 >= cur2:
                intervals[i] = [cur1, nex2]
                intervals.pop(i+1)
                continue
            if nex1 >= cur1 and nex2 <= cur2:
                intervals.pop(i+1)
                continue
            i += 1
        if not used:
            intervals.append(newInterval)
        return intervals


            