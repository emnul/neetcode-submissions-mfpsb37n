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
            # case 1 no left sub tree
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
            # case 2 left subtree exists
                # find in order predessor, rightmost value of left subtree
                # make a thread back to cur
                # go left
                predecessor = cur
                predecessor = predecessor.left
                while predecessor.right and predecessor.right != cur:
                    predecessor = predecessor.right
                
                # already made a thread
                if predecessor.right == cur:
                    predecessor.right = None
                    res.append(cur.val)
                    cur = cur.right
                else:
                    # first time at predecessor for cur
                    predecessor.right = cur
                    cur = cur.left
        return res


                

                


        