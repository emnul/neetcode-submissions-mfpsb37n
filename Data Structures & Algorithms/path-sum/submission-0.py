# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        pathSum = 0
        if not root:
            return False
        
        pathSum += root.val

        # cur node has no children
        if not root.left and not root.right:
            return targetSum - pathSum == 0
        elif self.hasPathSum(root.left, targetSum - pathSum):
            return True
        elif self.hasPathSum(root.right, targetSum - pathSum):
            return True
        
        return False

