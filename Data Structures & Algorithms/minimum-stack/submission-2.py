class MinStack:

    def __init__(self):
        self.stack = []
        self.m = float('inf')
        
    def push(self, val: int) -> None:
        self.m = min(val, self.m)
        self.stack.append([val, self.m])

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.m = self.stack[-1][1]
        else:
            self.m = float('inf')
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
