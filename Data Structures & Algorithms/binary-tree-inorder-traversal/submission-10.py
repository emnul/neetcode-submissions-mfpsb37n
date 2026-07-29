# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        callStack = []
        res = []

        if not root:
            return res
        
        cur = root
        while cur or callStack:
            while cur:
                callStack.append(cur)
                cur = cur.left
            cur = callStack.pop()
            res.append(cur.val)
            cur = cur.right
        
        return res