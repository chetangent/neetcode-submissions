class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p = []
        for i in range(len(position)):
            p.append((position[i], speed[i]))
        p.sort()
        t = [0] * len(position)
        for i, (po, s) in enumerate(p):
            t[i] = (target - po)/s
        stack = []
        t = t[::-1]
        for i in t:
            if not stack or i > stack[-1]:
                stack.append(i)
        return len(stack)