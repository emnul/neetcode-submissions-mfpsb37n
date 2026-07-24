# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        print(root.val)

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # handle 0, 1 children case
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # handle 2 children case
            # replace node with in order successor
            # leftmost value of right subtree
            successor = root
            rParent = None
            successor = successor.right
            while successor.left:
                rParent = successor
                successor = successor.left
            
            if rParent:
                rParent.left = successor.right
                successor.right = root.right
            
            successor.left = root.left

            return successor
            
        
        return root