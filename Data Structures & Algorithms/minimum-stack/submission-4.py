class MinStack:

    def __init__(self):
        self.stack = []
        self.smallest_history = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.smallest_history) == 0:
            self.smallest_history.append(val)
        elif val <= self.smallest_history[-1]:
            self.smallest_history.append(val)

    def pop(self) -> None:
        if self.smallest_history[-1] == self.stack[-1]:
            self.smallest_history.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smallest_history[-1]
