class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []
        

    def push(self, val: int) -> None:
        if not self.stack: # if stack is empty
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack: # is stack is empty
            return

        pop = self.stack.pop()
        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        t = self.stack[-1]

        if t > 0:
            return self.min + t
        else:
            return self.min
        

    def getMin(self) -> int:
        return self.min
