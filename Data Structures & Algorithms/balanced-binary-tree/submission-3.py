# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root): # return [balance, height]
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            # left subtree, right subtree and tree from current root must all be balanced
            balanced = (left[0] and right[0] and
                        abs(left[1] - right[1]) <= 1)
            height = max(left[1], right[1])
            return [balanced, height + 1]
        return dfs(root)[0]