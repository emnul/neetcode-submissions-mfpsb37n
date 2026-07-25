# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        levels = []

        def bfs(root):
            q = collections.deque()

            if root:
                q.append(root)
            
            while len(q) > 0:
                nodes = []
                for i in range(len(q)):
                    n = q.popleft()
                    nodes.append(n.val)
                    if n.right:
                        q.append(n.right)
                    if n.left:
                        q.append(n.left)
                levels.append(nodes)

        bfs(root)

        for l in levels:
            res.append(l[0])
        
        return res
                


