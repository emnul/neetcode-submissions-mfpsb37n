from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.items = 0      

    def push(self, x: int) -> None:
        self.items += 1
        tmp = []
        # empty queue
        while self.q1:
            tmp.append(self.q1.popleft())
        tmp.reverse()
        tmp.append(x)
        while tmp:
            self.q1.append(tmp.pop())

        

    def pop(self) -> int:
        self.items -= 1
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]
        
    def empty(self) -> bool:
        return self.items == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()