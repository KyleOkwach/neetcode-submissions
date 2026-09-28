class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        print(self.stack)

        self.stack.append(val)

    def pop(self) -> None:
        print(self.stack)

        if self.stack:
            del self.stack[-1]

    def top(self) -> int:
        print(self.stack)

        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        print(self.stack)

        if self.stack:
            return min(self.stack)
