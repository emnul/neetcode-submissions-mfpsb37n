# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0

        # returns height
        def dfs(root):
            nonlocal diameter
            if not root:
                return 0
            
            hL = dfs(root.left)
            hR = dfs(root.right)

            diameter = max(diameter, hL + hR)

            return max(hL, hR) + 1
        
        dfs(root)

        return diameter