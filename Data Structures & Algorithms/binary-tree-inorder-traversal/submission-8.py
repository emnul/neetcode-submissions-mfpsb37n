# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        cur = root
        while cur:
            # case 1 no left subtree
            # append and go right
            if not cur.left:
                res.append(cur.val)
                cur = cur.right # take us back to parent if visited already
            # case 2 left subtree exists
            else:
                # find in order predecessor
                # rightmost value of left subtree
                predecessor = cur
                predecessor = predecessor.left
                while predecessor.right and predecessor.right != cur:
                    predecessor = predecessor.right
                
                # check if visited already
                if predecessor.right == cur:
                    predecessor.right = None
                    res.append(cur.val)
                    cur = cur.right 
                else:
                    predecessor.right = cur
                    cur = cur.left
        return res
                


        
            
