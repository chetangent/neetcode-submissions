class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m, ss = 0, set()
        l = 0
        for h in range(len(s)):
            if s[h] not in ss:
                ss.add(s[h])
            else:
                while s[l]!=s[h]:
                    ss.remove(s[l])
                    l+=1
                l+=1
            m = max(m, h - l + 1)
        return m