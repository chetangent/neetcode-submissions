class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        count = [[] for i in range(len(nums) + 1)]
        for i, j in d.items():
            count[j].append(i)
        res = []
        for i in range(len(nums), 0, -1):
            for j in count[i]:
                res.append(j)
                if len(res)==k:
                    return res


