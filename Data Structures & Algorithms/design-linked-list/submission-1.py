class Node:
    def __init__(self, val, prev = None, nextNode = None):
        self.val = val
        self.prev = prev
        self.next = nextNode

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        cur = self.head.next
        while cur and index > 0:
            index -= 1
            cur = cur.next
        if cur and cur != self.tail and index == 0:
            return cur.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.head, self.head.next)
        prev, next = self.head, self.head.next
        prev.next = node
        next.prev = node        

    def addAtTail(self, val: int) -> None:
        node = Node(val, self.tail.prev, self.tail)
        prev, next = self.tail.prev, self.tail
        prev.next = node
        next.prev = node     
        
    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head.next
        while cur and index > 0:
            index -= 1
            cur = cur.next
        if cur and index == 0:
            node = Node(val, cur.prev, cur)
            prev, next = cur.prev, cur
            prev.next = node
            next.prev = node     
        

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next
        while cur and index > 0:
            index -= 1
            cur = cur.next
        if cur and cur != self.tail and index == 0:
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