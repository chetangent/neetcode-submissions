class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        m=0
        for i in nums:
            if i-1 in s:
                continue
            else:
                curr, x = 1, i+1
                while x in s:
                    curr+=1
                    x+=1
                m=max(m, curr)
        return m