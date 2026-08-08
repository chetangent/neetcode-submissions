class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        heap = [[grid[0][0], 0, 0]]
        visit = set()
        directions = [[0, 1], [0, -1], [1,0], [-1,0]]
        visit.add((0, 0))
        while heap:
            t, r, c = heapq.heappop(heap)
            visit.add((r, c))
            if r==n-1 and c==n-1:
                return t
            for dr, dc in directions:
                rr = r+dr
                cc = c+dc
                if rr<0 or rr==n or cc<0 or cc==n or (rr, cc) in visit:
                    continue
                heapq.heappush(heap, [max(t, grid[rr][cc]), rr, cc])
                visit.add((rr, cc))