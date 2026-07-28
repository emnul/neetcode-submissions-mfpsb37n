# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        order = []

        while head:
            order.append(head.val)
            head = head.next
        
        cur = dummy
        for i in range(len(order) - 1, -1, -1):
            cur.next = ListNode(order[i])
            cur = cur.next
        
        return dummy.next
        