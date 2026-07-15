class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity


    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # Increase capacity and copy array elements
        # over to new array
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1
        

    def popback(self) -> int:
        self.size -= 1
        tmp = self.arr[self.size]
        return tmp

    def resize(self) -> None:
        tmp = self.arr.copy()
        self.capacity = self.capacity * 2
        self.arr = [0] * self.capacity

        for i, e in enumerate(tmp):
            self.arr[i] = e

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
