class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}
        for i in tokens:
            if i not in ops:
                stack.append(int(i))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                if i == "+":
                    n3 = n1 + n2
                elif i == "-":
                    n3 = n1 - n2
                elif i == "*":
                    n3 = n1 * n2
                elif i == "/":
                    n3 = int(n1/n2)
                stack.append(n3)
        return stack[-1]