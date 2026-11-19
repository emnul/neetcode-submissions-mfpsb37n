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
            
            isLeftBal, lHeight = dfs(root.left)
            isRightBal, rHeight = dfs(root.right)

            balanced = isLeftBal and isRightBal and abs(lHeight - rHeight) < 2

            return [balanced, max(lHeight, rHeight) + 1]
        
        return dfs(root)[0]