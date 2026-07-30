class ListNode:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, index: int) -> int:
        cur = self.head.next
        while cur and index > 0:
            index -= 1
            cur = cur.next
        
        if cur and index == 0 and cur != self.tail:
            return cur.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val, self.head, self.head.next)
        prev, next = self.head, self.head.next
        prev.next = newNode
        next.prev = newNode

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val, self.tail.prev, self.tail)
        prev, next = self.tail.prev, self.tail
        prev.next = newNode
        next.prev = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            newNode = ListNode(val, cur.prev, cur)
            prev, next = cur.prev, cur
            prev.next = newNode
            next.prev = newNode

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next
        while cur and index > 0:
            index -= 1
            cur = cur.next
        
        if cur and index == 0 and cur != self.tail:
            prev, next = cur.prev, cur.next
            prev.next = next
            next.prev = prev

            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)