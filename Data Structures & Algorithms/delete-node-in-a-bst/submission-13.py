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
        
        parent = None
        cur = root
        while cur:
            if cur.val < key:
                parent = cur
                cur = cur.right
            elif cur.val > key:
                parent = cur
                cur = cur.left
            else:
                break
        
        if not cur:
            return root
        
        # found value, remove from tree
        # cur only has 1 child
        if not cur.left:
            if not parent:
                return cur.right
            else:
                if cur == parent.left:
                    parent.left = cur.right
                else:
                    parent.right = cur.right
                return root
        elif not cur.right:
            if not parent:
                return cur.left
            else:
                if cur == parent.left:
                    parent.left = cur.left
                else:
                    parent.right = cur.left
                return root
        # 2 two child case, replace with in order successor
        # leftmost value in right subtree
        else:
            delNode = cur
            rParent = None
            cur = cur.right
            while cur.left:
                rParent = cur
                cur = cur.left
            
            if rParent:
                rParent.left = cur.right
                cur.right = delNode.right
            
            cur.left = delNode.left
            
            if not parent:
                return cur
            else:
                if parent.left == delNode:
                    parent.left = cur
                else:
                    parent.right = cur
                return root


                
        

        
