# Doubly Linked List Node
class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        

    def append(self, value: int) -> None:
        lastNode = self.tail.prev
        newNode = ListNode(value, lastNode, self.tail)

        lastNode.next = newNode
        self.tail.prev = newNode
        

    def appendleft(self, value: int) -> None:
        firstNode = self.head.next
        newNode = ListNode(value, self.head, firstNode)

        firstNode.prev = newNode
        self.head.next = newNode

    def pop(self) -> int:
        if not self.isEmpty():
            targetNode = self.tail.prev
            val = targetNode.val
            prevNode = targetNode.prev

            prevNode.next = self.tail
            self.tail.prev = prevNode
            return val
        
        return -1
        

    def popleft(self) -> int:
        if not self.isEmpty():
            targetNode = self.head.next
            val = targetNode.val
            nextNode = targetNode.next

            nextNode.prev = self.head
            self.head.next = nextNode
            return val
        
        return -1
        
