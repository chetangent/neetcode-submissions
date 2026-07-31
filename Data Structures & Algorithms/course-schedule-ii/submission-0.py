class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        r = set()
        pre = defaultdict(list)
        visit = set()
        for c, p in prerequisites:
            pre[c].append(p)
        def dfs(c):
            if c in visit:
                return False
            if not pre[c]:
                if c not in r:
                    r.add(c)
                    res.append(c)
                return True
            visit.add(c)
            for p in pre[c]:
                if not dfs(p):
                    return False
            visit.remove(c)
            pre[c] = []
            if c not in r:
                    r.add(c)
                    res.append(c)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res