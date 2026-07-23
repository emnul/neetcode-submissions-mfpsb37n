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
        curr = root

        # find node to delete
        while curr and curr.val != key:
            parent = curr
            if key > curr.val:
                curr = curr.right
            else:
                curr = curr.left

        # node not found, return original root
        if not curr:
            return root

        # node with only child or no child
        if not curr.left or not curr.right:
            child = curr.left if curr.left else curr.right
            # check if we're at the root
            if not parent:
                return child

            if parent.left == curr:
                parent.left = child
            else:
                parent.right = child
            
        # two children
        else:
            par = None # parent of right subTree min node
            delNode = curr
            curr = curr.right
            while curr.left:
                par = curr
                curr = curr.left
            
            if par: # if there was a left traversal
                par.left = curr.right
                curr.right = delNode.right

            curr.left = delNode.left

            if not parent: # if we're deleting root
                return curr

            if parent.left == delNode:
                parent.left = curr
            else:
                parent.right = curr

        
        return root

