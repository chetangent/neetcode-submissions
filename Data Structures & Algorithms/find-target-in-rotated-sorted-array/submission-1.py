class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        while l <= h:
            mid = l + (h - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[h]:
                if nums[mid] < target or nums[l] > target:
                    l = mid + 1
                else:
                    h = mid - 1
            else:
                if nums[mid] > target or nums[h] < target:
                    h = mid - 1
                else:
                    l = mid + 1
        return -1