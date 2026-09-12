class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.minStack and val > self.minStack[-1]:
            self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        if not self.stack:
            return
        return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.stack:
            return
        return self.minStack[-1]
        
