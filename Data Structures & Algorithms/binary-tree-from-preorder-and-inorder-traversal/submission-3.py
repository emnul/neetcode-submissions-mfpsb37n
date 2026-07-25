# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorderInd = 0
        self.preorderInd = 0

        def dfs(limit): # builds a subtree until we hit limit value
            if self.preorderInd >= len(preorder):
                return None
            if inorder[self.inorderInd] == limit:
                self.inorderInd += 1
                return None
            
            root = TreeNode(preorder[self.preorderInd])
            self.preorderInd += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        
        return dfs(float('inf'))
