# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            
            if not root:
                return [True, 0]

            [lBalance, lHeight] = dfs(root.left)
            [rBalance, rHeight] = dfs(root.right)

            height = max(lHeight, rHeight)

            if abs(lHeight - rHeight) > 1:
                return [False, height + 1]
            elif not lBalance or not rBalance:
                return [False, height + 1]
            else:
                return [True, height + 1]
            
        
        return dfs(root)[0]