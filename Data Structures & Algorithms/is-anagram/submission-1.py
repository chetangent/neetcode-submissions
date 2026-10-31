class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for j in t:
            if j not in d:
                return False
            d[j] -= 1
            if d[j] == 0:
                del d[j]
        return not d