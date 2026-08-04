# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = 0
        inorderValToIdx = {val:ind for ind, val in enumerate(inorder)}

        # use array limits to avoid O(N) lookups
        def dfs(l, r):
            nonlocal preIdx
            if l > r or preIdx >= len(preorder):
                return None
            
            root = TreeNode(preorder[preIdx])
            preIdx += 1
            mid = inorderValToIdx[root.val]
            # build left subtree
            root.left = dfs(l, mid - 1)
            # build right subtree
            root.right = dfs(mid + 1, r)

            return root
        
        return dfs(0, len(preorder) - 1)

