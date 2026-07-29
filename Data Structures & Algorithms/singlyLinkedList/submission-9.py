class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        cur = self.head.next
        while cur and index > 0:
            index -= 1
            cur = cur.next
        if cur and index == 0:
            return cur.val
        return -1
        

    def insertHead(self, val: int) -> None:
        node = ListNode(val, self.head.next)
        self.head.next = node

        if self.tail == self.head:
            self.tail = self.head.next

    def insertTail(self, val: int) -> None:
        node = ListNode(val, None)
        self.tail.next = node
        self.tail = node

    def remove(self, index: int) -> bool:
        cur = self.head
        while cur and index > 0:
            index -= 1
            cur = cur.next
        if cur and cur.next and index == 0:
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
        
