class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)
        for c, p in prerequisites:
            pre[c].append(p)
        visit = set()
        def dfs(c):
            if c in visit:
                return False
            if not pre[c]:
                return True
            visit.add(c)
            for p in pre[c]:
                if not dfs(p):
                    return False
            visit.remove(c)
            pre[c] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True