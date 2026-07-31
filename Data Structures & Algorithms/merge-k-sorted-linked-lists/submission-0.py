# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        numLists = len(lists)
        res = []
        for i in range(numLists):
            cur = lists[i]
            while cur:
                res.append(cur.val)
                cur = cur.next
        
        res.sort()
        if not res:
            return None
        head = ListNode(res[0])
        cur = head
        for i in range(1, len(res)):
            cur.next = ListNode(res[i])
            cur = cur.next
        return head

            
        