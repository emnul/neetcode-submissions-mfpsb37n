class Solution:
    def dfs(self, crs, adjList, visit, path):
        if crs in visit and crs in path:
            return False
        
        visit.add(crs)
        path.add(crs)

        for neighbor in adjList[crs]:
            if not self.dfs(neighbor, adjList, visit, path): return False
        
        adjList[crs] = []
        path.remove(crs)

        return True

    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = collections.defaultdict(list)

        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        visit = set() # prevent us from visiting same node when running dfs
        path = set() # detect cycles along current path

        # need to run dfs on each node to account for disconnect graph
        for crs in range(numCourses):
            # detected a cycle
            if not self.dfs(crs, adjList, visit, path): return False
        
        return True
