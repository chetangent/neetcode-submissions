class Solution:
    def isValid(self, s: str) -> bool:
        o = {"(", "[", "{"}
        c = {")": "(", "]": "[", "}": "{"}
        stack = []
        for i in s:
            if i in o:
                stack.append(i)
            else:
                if stack and stack[-1] == c[i]:
                    stack.pop()
                else:
                    return False
        return not stack