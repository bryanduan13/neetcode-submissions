class DynamicArray:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size= 0
        self.array = [None] * self.cap 

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.cap:
            self.resize()
        self.set(self.size,n)
        self.size = self.size +1 

    def popback(self) -> int:
        self.size = self.size -1
        return self.get(self.size) 

    def resize(self) -> None:
        newArr = [None] * (self.cap*2)
        for t in range (self.size):
            newArr[t] = self.array[t]
        self.array = newArr
        self.cap *=2
        

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.cap