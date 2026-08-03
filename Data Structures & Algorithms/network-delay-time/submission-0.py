class Solution:
    def networkDelayTime(self, times: List[List[int]], nn: int, k: int) -> int:
        edges = defaultdict(list)
        for u,v,w in times:
            edges[u].append([v, w])
        time = 0
        heap = [[0, k]]
        visit = set()
        while heap:
            t, n = heapq.heappop(heap)
            if n in visit:
                continue
            visit.add(n)
            time = max(time, t)
            for nei, w in edges[n]:
                if nei not in visit:
                    heapq.heappush(heap, [t+w, nei])
        return time if len(visit) == nn else -1
