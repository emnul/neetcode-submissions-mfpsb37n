# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inInd = preInd = 0

        def recurse(limit):
            nonlocal inInd, preInd

            if preInd >= len(preorder) or inorder[inInd] == limit:
                return None
            
            root = TreeNode(preorder[preInd])
            preInd += 1
            inorderLim = root.val
            root.left = recurse(inorderLim)
            inInd += 1
            root.right = recurse(limit)



            return root
        
        return recurse(float('inf'))

        