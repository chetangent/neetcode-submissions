class Solution:
    def minEatingSpeed(self, piles: List[int], hours: int) -> int:
        l, h = 1, max(piles)
        while l <= h:
            count = 0
            mid = l + (h - l) // 2
            for p in piles:
                count += p//mid
                if p%mid != 0:
                    count += 1
            if count <= hours:
                h = mid - 1
            else:
                l = mid + 1
        return l
        
                
