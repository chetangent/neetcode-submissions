class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = 0
        for i in digits:
            n*=10
            n+=i
        n+=1
        digits = []
        while n:
            digits = [n%10]+digits
            n//=10
        return digits