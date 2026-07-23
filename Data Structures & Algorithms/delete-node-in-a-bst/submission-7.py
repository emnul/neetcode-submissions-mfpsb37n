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

        # track parent and curr
        parent = None
        curr = root

        # search for key
        while curr and curr.val != key:
            if key > curr.val:
                parent = curr
                curr = curr.right
            else:
                parent = curr
                curr = curr.left
        
        # check if found key
        if not curr:
            return root
        
        # remove node with 0 or 1 children
        if not curr.left or not curr.right:
            child = curr.left if curr.left else curr.right

            if curr == root:
                return child
            
            if parent.left == curr:
                parent.left = child
            else:
                parent.right = child
        else:
            # remove node with 2 children
            rParent = None
            delNode = curr
            # find in order successor of right subtree
            curr = curr.right
            while curr.left:
                rParent = curr
                curr = curr.left
            
            # left traversal
            if rParent:
                # curr is min node in right subtree
                rParent.left = curr.right
                curr.right = delNode.right
            
            curr.left = delNode.left
            
            if not parent:
                return curr
            elif parent.left == delNode:
                parent.left = curr
            else:
                parent.right = curr

            
            
        return root



