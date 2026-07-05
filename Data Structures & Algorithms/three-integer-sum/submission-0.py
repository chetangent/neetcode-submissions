class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            l, h = i+1, len(nums)-1
            while l<h:
                s=nums[i]+nums[l]+nums[h]
                if s==0:
                    res.append([nums[i], nums[l], nums[h]])
                    l+=1
                    h-=1
                    while l<h and nums[l]==nums[l-1]:
                        l+=1
                    while l<h and nums[h]==nums[h+1]:
                        h-=1
                elif s<0:
                    l+=1
                elif s>0:
                    h-=1
        return res


