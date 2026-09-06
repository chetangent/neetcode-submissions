class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            local = 0
            j = i
            while j:
                local+=j%2
                j//=2
            res.append(local)
        return res