# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        # we do dfs until we reach a left node and return, we pop up
        # the stack swap left and right node, then return current node with swapped
        # left and right
        def dfs(r):
            if not r:
                return None
            
            left = dfs(r.left)
            right = dfs(r.right)

            return TreeNode(r.val, right, left)


        return dfs(root)
