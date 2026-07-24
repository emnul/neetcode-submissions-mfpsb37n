# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []
        cur = root
        kth = 0
        while cur or stack:
            stack.append(cur)
            cur = cur.left

            if not cur:
                cur = stack.pop()
                kth += 1
                
                if kth == k:
                    return cur.val
            
                while not cur.right:
                    cur = stack.pop()
                    kth += 1
                
                    if kth == k:
                        return cur.val
            
                cur = cur.right
        
        