class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = collections.defaultdict(list)
        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        # node is curr node and visit is 
        # set of nodes we've visited along the current path
        def dfs(node, visit):
            if node in visit:
                return False
            if not adjList[node]:
                return True
            
            visit.add(node)
            for nei in adjList[node]:
                if not dfs(nei, visit):
                    return False
            visit.remove(node)
            adjList[node] = []
            return True
        
        for i in range(numCourses):
            canFinish = dfs(i, set())
            if not canFinish:
                return False
        
        return True