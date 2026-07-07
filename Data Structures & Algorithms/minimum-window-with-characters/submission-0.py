class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        dt, window = {}, {}
        for i in t:
            dt[i] = 1 + dt.get(i, 0)
        l = 0
        have, need = 0, len(dt)
        ran = [-1, -1]
        m = float('inf')
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in dt and window[c]==dt[c]:
                have += 1
            while have == need:
                if r-l+1 < m:
                    m = r-l+1
                    ran = [l, r]
                c=s[l]
                window[c]-=1
                if c in dt and window[c]<dt[c]:
                    have -= 1
                l+=1
        if m == float('inf'):
            return ""
        l, r = ran
        return s[l:r+1]

