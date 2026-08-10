class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        total = sum(nums)
        if total%2:
            return False
        total/=2
        for i in range(len(nums)-1, -1, -1):
            if nums[i]<=total:
                total-=nums[i]
        return not total