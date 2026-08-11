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

        while cur and cur.val != key:
            if cur.val < key:
                parent = cur
                cur = cur.right
            else:
                parent = cur
                cur = cur.left
        
        if not cur:
            return root

        # found key
        if not cur.left:
            if parent:
                if parent.left == cur:
                    parent.left = cur.right
                else:
                    parent.right = cur.right
            else:
                root = root.right
        elif not cur.right:
            if parent:
                if parent.left == cur:
                    parent.left = cur.left
                else:
                    parent.right = cur.left
            else:
                root = root.left
        else:
            # cur has two children
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

            if parent:
                if parent.left == delNode:
                    parent.left = cur
                else:
                    parent.right = cur
            else:
                return cur

        return root
                
        
