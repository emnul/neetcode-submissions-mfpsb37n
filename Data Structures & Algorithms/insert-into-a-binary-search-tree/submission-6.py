# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val) 

        parent = None
        cur = root
        while cur:
            parent = cur
            if cur.val > val:
                cur = cur.left
            else:
                cur = cur.right

        if not parent:
            if root.val > val:
                root.left = TreeNode(val)
            else:
                root.right = TreeNode(val)
        else:
            if parent.val > val:
                parent.left = TreeNode(val)
            else:
                parent.right = TreeNode(val)
        
        return root