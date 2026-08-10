class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        leng = 0
        for i in range(len(s)):
            l, h = i, i
            while l>=0 and h<len(s) and s[l]==s[h]:
                l-=1
                h+=1
            if h-l-1>leng:
                leng=h-l-1
                res = s[l+1:h]
            l, h = i, i+1
            while l>=0 and h<len(s) and s[l]==s[h]:
                l-=1
                h+=1
            if h-l-1>leng:
                leng=h-l-1
                res = s[l+1:h]
        return res