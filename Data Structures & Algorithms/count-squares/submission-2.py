class CountSquares:

    def __init__(self):
        self.hash = defaultdict(int)

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        self.hash[point]+=1

    def count(self, point: List[int]) -> int:
        keys = list(self.hash.keys())
        res = 0
        for i, j in keys:
            if abs(point[0]-i)!=abs(point[1]-j) or i==point[0] or j==point[1]:
                continue
            res+= self.hash[(point[0], j)]*self.hash[(i, point[1])] * self.hash[(i, j)]
        return res
