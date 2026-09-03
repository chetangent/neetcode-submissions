class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = float("-inf")
        m = max(nums)
        for i in nums:
            if curr<0 and i>0:
                curr = i
            else:
                curr+=i
            m = max(m, curr)
        return m