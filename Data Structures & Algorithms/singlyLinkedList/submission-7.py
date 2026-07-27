class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = Node(0)
        self.tail = self.head

    def get(self, index: int) -> int:
        i = 0
        cur = self.head.next
        while cur:
            if i == index:
                return cur.val
            i += 1
            cur = cur.next
        return -1
        

    def insertHead(self, val: int) -> None:
        self.head.next = Node(val, self.head.next)

        if self.tail == self.head:
            self.tail = self.head.next
        
        

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        i = 0
        cur = self.head
        while cur.next and i != index:
            i += 1
            cur = cur.next
        
        if cur.next:
            # removing tail
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            return True

        return False
        

    def getValues(self) -> List[int]:
        values = []
        cur = self.head.next

        while cur:
            values.append(cur.val)
            cur = cur.next
        return values
        
