class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        def robb(num):
            if len(num)<3:
                return max(num)
            num[1]=max(num[0], num[1])
            for i in range(2, len(num)):
                num[i]=max(num[i]+num[i-2], num[i-1])
            return num[-1]
        return max(robb(nums[1:]), robb(nums[:-1]))