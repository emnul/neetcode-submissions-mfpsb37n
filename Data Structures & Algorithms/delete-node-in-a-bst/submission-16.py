# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    
        def dfs(root):
            if not root:
                return None
            
            if root.val < key:
                root.right = dfs(root.right)
            elif root.val > key:
                root.left = dfs(root.left)
            else:
                # check for children
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    # replace with in order sucessor
                    cur = root
                    cur = cur.right
                    rParent = None

                    while cur.left:
                        rParent = cur
                        cur = cur.left
                    
                    if rParent:
                        rParent.left = cur.right
                        cur.right = root.right
                    
                    cur.left = root.left
                    return cur
            
            return root

        
        return dfs(root)