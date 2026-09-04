class Solution:
    def isHappy(self, n: int) -> bool:
        def sum(n):
            res = 0
            while n:
                res += (n%10)**2
                n//=10
            return res
        seen = set()
        while n not in seen:
            n = sum(n)
            if n<10:
                seen.add(n)
            if n==1:
                return True
        return False