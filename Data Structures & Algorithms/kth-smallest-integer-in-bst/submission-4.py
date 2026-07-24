# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = root
        while cur:
            # case 1 no left node
            if not cur.left:
                k -= 1
                if k == 0:
                    return cur.val
                cur = cur.right
            # case 2 left node exists
            # find in order predecessor
            # rightmost value of left subtree
            else:
                predecessor = cur
                predecessor = predecessor.left
                while predecessor.right and predecessor.right != cur:
                    predecessor = predecessor.right
                
                # check if visited
                if predecessor.right == cur:
                    predecessor.right = None
                    k -= 1
                    if k == 0:
                        return cur.val
                    cur = cur.right
                else:
                    predecessor.right = cur
                    cur = cur.left
