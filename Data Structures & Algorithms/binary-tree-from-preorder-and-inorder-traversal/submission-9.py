# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inIdx = preInd = 0

        # limit defines boundaries for inorder
        def dfs(limit):
            nonlocal preInd, inIdx

            if preInd >= len(preorder) or inorder[inIdx] == limit:
                return None
            
            root = TreeNode(preorder[preInd])
            # we immediately increment preInd
            # preorder traversal processes node before moving to left subtree
            preInd += 1
            nextLimit = root.val
            root.left = dfs(nextLimit)
            # we increment inIdx when we're done with the left subtree
            # recall that inorder traversal processes left subtree first
            inIdx += 1
            root.right = dfs(limit)

            return root

        return dfs(float('inf'))