class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        res = [0] * (len(num1)+len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                index = i+j
                digit = int(num1[i])*int(num2[j])
                res[index]+=digit
                res[index+1]+=res[index]//10
                res[index]%=10
        res = res[::-1]
        beg = 0
        while beg<len(res) and res[beg]==0:
            beg+=1
        out = ""
        for i in res[beg:]:
            out+=str(i)
        return out
        