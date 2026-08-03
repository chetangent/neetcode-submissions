class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = {i:[] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                edges[i].append([dist, j])
                edges[j].append([dist, i])
        res = 0
        visit = set()
        heap = [[0, 0]]
        while len(visit)<n:
            w, node = heapq.heappop(heap)
            if node in visit:
                continue
            visit.add(node)
            res+=w
            for neiw, nei in edges[node]:
                if nei in visit:
                    continue
                heapq.heappush(heap, [neiw, nei])
        return res