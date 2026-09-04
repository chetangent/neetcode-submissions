class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        start, end = newInterval[0], newInterval[1]
        for i, j in intervals:
            if i<=start and j>=start:
                start = i
            if i<=end and j>=end:
                end = j
        for i, j in intervals:
            if j<start or i>end:
                output.append([i, j])
        output.append([start, end])
        output.sort()
        return output


