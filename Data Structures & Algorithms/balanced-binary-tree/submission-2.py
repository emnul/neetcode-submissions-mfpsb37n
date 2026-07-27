# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root): # returns [isBalanced, height]
            if not root:
                return [True, 0]
            
            [lBalanced, lHeight] = dfs(root.left)
            [rBalanced, rHeight] = dfs(root.right)

            height = max(lHeight, rHeight)
            if abs(lHeight - rHeight) > 1 or not lBalanced or not rBalanced:
                return [False, height + 1]
            else:
                return [True, height + 1]

        return dfs(root)[0]