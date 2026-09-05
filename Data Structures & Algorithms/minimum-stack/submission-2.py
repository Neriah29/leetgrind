class MinStack:
    """
    self.min = [1]
    self.stack = [1,2]
    """
    def __init__(self):
        self.minimum = []
        self.stack = []


    def push(self, val: int) -> None:
        if (not self.minimum) or (self.minimum and val <= self.minimum[-1]):
            self.minimum.append(val)

        self.stack.append(val)


    def pop(self) -> None:
        cur = self.stack.pop()
        if cur == self.minimum[-1]:
            self.minimum.pop() 

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
