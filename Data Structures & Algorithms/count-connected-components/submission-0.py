class Solution:
    def countComponents(self, nn: int, edges: List[List[int]]) -> int:
        comp = 0
        visit = set()
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        def dfs(n, prev):
            if n in visit:
                return
            visit.add(n)
            for nei in graph[n]:
                if nei==prev:
                    continue
                dfs(nei, n)
        for n in range(nn):
            if n in visit:
                continue
            comp += 1
            dfs(n, -1)
        return comp