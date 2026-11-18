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
            
            isLeftBalanced, leftHeight = dfs(root.left)
            isRightBalanced, rightHeight = dfs(root.right)

            balance = isLeftBalanced and isRightBalanced and abs(leftHeight - rightHeight) < 2

            return [balance, max(leftHeight, rightHeight) + 1]

        return dfs(root)[0]

