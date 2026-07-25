class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
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
        new_node = Node(val, self.head.next)
        self.head.next = new_node

        if self.tail == self.head:
            self.tail = new_node

        

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        i = 0
        cur = self.head
        while i < index:
            cur = cur.next
            i += 1
        
        if cur and cur.next:
            # check for removing tail
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
        
