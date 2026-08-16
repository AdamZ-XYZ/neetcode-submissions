class DynamicArray:

    size = 0
    array_capacity = 0
    dynamicArray = []
    
    def __init__(self, capacity: int):
        self.dynamicArray = [0] * capacity
        self.array_capacity = capacity

    def get(self, i: int) -> int:
        return self.dynamicArray[i]

    def set(self, i: int, n: int) -> None:
        self.dynamicArray[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.array_capacity :
            self.resize()
        size = self.size    
        self.dynamicArray[size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.dynamicArray[self.size]

    def resize(self) -> None:
        list = [0] * (self.array_capacity * 2)
        self.array_capacity = self.array_capacity*2
        for i in range(self.size):
            list[i] = self.dynamicArray[i]
            i += 1
        self.dynamicArray = list

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.array_capacity