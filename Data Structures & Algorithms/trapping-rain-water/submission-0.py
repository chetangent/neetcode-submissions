class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, h = 0, len(height)-1
        lm, rm = height[0], height[-1]
        res = 0
        while l<h:
            if lm<rm:
                l+=1
                lm=max(lm, height[l])
                res+=lm-height[l]
            else:
                h-=1
                rm=max(rm, height[h])
                res+=rm-height[h]
        return res