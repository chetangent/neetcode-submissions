class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        l, r = 0, 0
        while r < len(prices) - 1:
            if prices[r]<prices[l]:
                l = r
            else:
                r+=1
                m = max(m, prices[r] - prices[l])
        return m