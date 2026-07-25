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
        while cur and i != index:
            cur = cur.next
            i += 1
        if cur:
            return cur.val
        return -1
        

    def insertHead(self, val: int) -> None:
        new_node = Node(val, self.head.next)
        self.head.next = new_node

        # Update tail if empty
        if self.tail == self.head:
            self.tail = new_node
        

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        cur = self.head
        i = 0
        while cur and i < index:
            cur = cur.next
            i += 1
 
        if cur and cur.next:
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
        
