class MinStack:

    def __init__(self):
        self.stack = []  
        self.minElement = [] #track min at each stack position

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minElement:
            self.minElement.append(val)
        else:
            val = min(self.minElement[-1], val)
            self.minElement.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.minElement.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minElement[-1]
        
