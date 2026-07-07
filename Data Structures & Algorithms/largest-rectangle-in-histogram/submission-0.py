class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        m = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                m = max(m, stack[-1][1]*(i - stack[-1][0]))
                start = stack[-1][0]
                stack.pop()
            stack.append((start, h))
        for i, h in stack:
            m = max(m, h*(len(heights)-i))
        return m    