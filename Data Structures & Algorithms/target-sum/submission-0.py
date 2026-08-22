class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def backtrack(i, num):
            if i==len(nums):
                return 1 if num==target else 0
            if (i, num) in cache:
                return cache[(i, num)]
            cache[(i, num)] = backtrack(i+1, num+nums[i]) + backtrack(i+1, num-nums[i])
            return cache[(i, num)]
        return backtrack(0, 0)