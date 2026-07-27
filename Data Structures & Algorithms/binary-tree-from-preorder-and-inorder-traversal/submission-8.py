# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # avoid an O(n) lookup in inorder for each iteration
        hm = {val:ind for ind, val in enumerate(inorder)}
        
        preInd = 0

        # we can avoid creating new arrays by passing indices that define the current subarray boundaries
        def dfs(l, r):
            nonlocal preInd

            if l > r:
                return None
            
            root = TreeNode(preorder[preInd])
            preInd += 1
            # mid tells us the # of nodes in the left subtree
            mid = hm[root.val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root

        return dfs(0, len(inorder) - 1)