class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        if not edges:
            return True
        graph = {i:[] for i in range(n)}
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        visit = set()
        def dfs(n, prev):
            if n in visit:
                return False
            visit.add(n)
            for nei in graph[n]:
                if nei == prev:
                    continue
                if not dfs(nei, n):
                    return False
            return True
        return dfs(0, -1) and len(visit) == n