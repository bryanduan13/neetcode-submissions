class MinStack:

    def __init__(self):
        self.array=[]
        self.minStack=[]
        self.stacklen=0

    def push(self, val: int) -> None:
        self.array.append(val)
        if self.stacklen == 0:
            self.minStack.append(val)
        elif val < self.minStack[self.stacklen-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[self.stacklen-1])
        self.stacklen+=1

    def pop(self) -> None:
        self.array.pop()
        self.minStack.pop()
        self.stacklen-=1

    def top(self) -> int:
        return self.array[self.stacklen-1]

    def getMin(self) -> int:
        return self.minStack[self.stacklen-1]
