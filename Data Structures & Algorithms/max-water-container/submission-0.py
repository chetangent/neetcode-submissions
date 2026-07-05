class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m=0
        l, h = 0, len(heights)-1
        while l<h:
            area = min(heights[l], heights[h]) * (h-l)
            m=max(m, area)
            if heights[l]<heights[h]:
                l+=1
            else:
                h-=1
        return m