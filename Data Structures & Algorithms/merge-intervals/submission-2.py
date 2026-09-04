class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        cs, ce = intervals[0][0], intervals[0][1]
        output = []
        for i, j in intervals:
            if i>ce:
                output.append([cs, ce])
                cs, ce = i, j
            elif i<=ce and i>=cs:
                ce = max(j, ce)
        output.append([cs, ce])
        return output