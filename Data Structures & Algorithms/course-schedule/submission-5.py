class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map courses to their prereqs
        adjList = collections.defaultdict(list)
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        # tracks all courses along curr DFS path
        visit = set()

        def dfs(crs):
            # detected a cycle
            if crs in visit:
                return False
            if adjList[crs] == []:
                return True
            
            visit.add(crs)
            for pre in adjList[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            adjList[crs] = []
            return True
        
        # need to check every course in case graph is not fully connected
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True