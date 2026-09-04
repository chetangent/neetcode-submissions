class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prev = intervals[0][1]
        for i, j in intervals[1:]:
            if i>=prev:
                prev = j
            else:
                res+=1
                prev = min(prev, j)
        return res