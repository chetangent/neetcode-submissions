class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        time, fresh = 0, 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                elif grid[r][c] == 1:
                    fresh+=1
        dirs = [[1, 0], [-1, 0], [0, 1], [0,-1]]
        while q and fresh:
            for i in range(len(q)):
                rr, cc = q.popleft()
                for dr, dc in dirs:
                    r=rr+dr
                    c=cc+dc
                    if r<0 or r==rows or c<0 or c==cols or grid[r][c]!=1:
                        continue
                    grid[r][c] = 2
                    q.append([r, c])
                    fresh -= 1
            time += 1
        return time if not fresh else -1

