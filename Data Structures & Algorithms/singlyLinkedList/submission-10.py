class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(0)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        cur = self.head.next
        while cur and index > 0:
            index -= 1
            cur = cur.next
        if cur:
            return cur.val
        return -1

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val, self.head.next)
        self.head.next = newNode

        if self.tail == self.head:
            self.tail = self.head.next
        

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val, None)
        self.tail.next = newNode
        self.tail = newNode
        

    def remove(self, index: int) -> bool:
        cur = self.head
        while cur.next and index > 0:
            index -= 1
            cur = cur.next
        if cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            return True
        return False
        

    def getValues(self) -> List[int]:
        cur = self.head.next
        values = []
        while cur:
            values.append(cur.val)
            cur = cur.next

        return values
        
