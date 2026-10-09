class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr = sorted(self.arr)
        return self.arr[-self.k]
        
