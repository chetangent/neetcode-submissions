class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        flag = False
        if x[0]=="-":
            flag = True
            x=x[1:]
        x=x[::-1]
        x=int(x)
        if x> 2**31:
            return 0
        return -1*x if flag else x