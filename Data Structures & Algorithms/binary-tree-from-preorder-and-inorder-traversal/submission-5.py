# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inInd = preInd = 0

        def dfs(limit): # builds a subtree until we hit limit value
            # using nonlocal allows an inner function to modify a variable defined in an 
            # outer function without creating a new local variable or accessing the module-level global scope.
            nonlocal preInd, inInd

            # no more nodes condition
            if preInd >= len(preorder):
                return None
            # done processing subtree
            if inorder[inInd] == limit:
                inInd += 1
                return None
            
            root = TreeNode(preorder[preInd])
            preInd += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        
        return dfs(float('inf'))
