class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p = []
        for i in range(len(position)):
            p.append((position[i], speed[i]))
        p.sort()
        t = [0] * len(position)
        for i, (po, s) in enumerate(p):
            t[i] = (target - po)/s
        count = 0
        time = float('-inf')
        for i in t[:: -1]:
            if i > time:
                count+=1
                time = i
        return count