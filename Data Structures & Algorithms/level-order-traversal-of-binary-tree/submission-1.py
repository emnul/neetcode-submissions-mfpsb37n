# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levelList = []
        q = collections.deque()
        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                e = q.popleft()
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
                level.append(e.val)
            levelList.append(level)
        
        return levelList
