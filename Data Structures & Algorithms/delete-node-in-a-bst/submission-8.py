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

        # search for key
        parent = None
        cur = root
        while cur and cur.val != key:
            if cur.val > key:
                parent = cur
                cur = cur.left
            elif cur.val < key:
                parent = cur
                cur = cur.right
    
        # if not found return root
        if not cur:
            return root

        # handle cur has 0, 1 children case
        if not cur.left:
            # handle case where delNode is root
            if not parent:
                return cur.right
            
            # otherwise del node and return root
            if parent.left == cur:
                parent.left = cur.right
            else:
                parent.right = cur.right

        elif not cur.right:
            # handle case where delNode is root
            if not parent:
                return cur.left
            
            # otherwise del node and return root
            if parent.left == cur:
                parent.left = cur.left
            else:
                parent.right = cur.left

        else: # 2 children case, replace with in order successor
            delNode = cur
            rParent = None
            # search for in order successor, leftmost value in right subtree
            cur = cur.right
            while cur.left:
                rParent = cur
                cur = cur.left

            if rParent:
                rParent.left = cur.right
                cur.right = delNode.right
            
            cur.left = delNode.left

            if not parent: # root check
                return cur
            
            # otherwise del node and return root
            if parent.left == delNode:
                parent.left = cur
            else:
                parent.right = cur
            

        return root






        # replace node with in order successor