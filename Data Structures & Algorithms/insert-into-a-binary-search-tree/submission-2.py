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
        
        curr = root
        while curr != None:
            if val > curr.val and curr.right:
                curr = curr.right
            elif val < curr.val and curr.left:
                curr = curr.left
            elif val > curr.val and not curr.right:
                curr.right = TreeNode(val)
                break
            elif val < curr.val and not curr.left:
                curr.left = TreeNode(val)
                break
        return root
            
        