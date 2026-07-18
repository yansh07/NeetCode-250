# Implement Stack Using Queues

class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        pop_elem = self.stack.pop()
        return pop_elem

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not self.stack