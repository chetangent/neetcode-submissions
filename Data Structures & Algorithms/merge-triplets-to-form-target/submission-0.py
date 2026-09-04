class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        f, s, t = False, False, False
        for i, j, k in triplets:
            if i==target[0] and j<=target[1] and k<=target[2]:
                f=True
            if j==target[1] and i<=target[0] and k<=target[2]:
                s=True
            if k==target[2] and j<=target[1] and i<=target[0]:
                t=True
        return f and s and t