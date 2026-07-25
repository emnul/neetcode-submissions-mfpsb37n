# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def bfs(root):
            q = collections.deque()

            if root:
                q.append(root)
            
            while len(q) > 0:
                rightMost = q[-1]
                for i in range(len(q)):
                    n = q.popleft()
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
                res.append(rightMost.val)

        bfs(root)
        
        return res
                


