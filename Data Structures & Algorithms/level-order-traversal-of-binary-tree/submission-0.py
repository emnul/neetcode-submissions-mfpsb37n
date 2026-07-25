# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def bfs(root):
            q = deque()

            if root:
                q.append(root)

            while len(q) > 0:
                nodes = []

                for i in range(len(q)):
                    n = q.popleft()
                    nodes.append(n.val)
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
                res.append(nodes)
            
        bfs(root)
        return res