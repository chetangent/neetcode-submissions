class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currmin, currmax = 1, 1
        for n in nums:
            if n == 0:
                currmin, currmax = 1, 1
                continue
            temp = n*currmax
            currmax = max(temp, n*currmin, n)
            currmin = min(temp, n*currmin, n)
            res = max(res, currmax)
        return res