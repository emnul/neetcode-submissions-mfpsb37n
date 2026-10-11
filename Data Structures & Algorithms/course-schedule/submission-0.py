class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = collections.defaultdict(list) # course num -> list of prereqs

        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        visit = set() # all courses along the cur DFS path
        
        def dfs(cNum):
            if not preMap[cNum]:
                return True
            # detected a loop
            if cNum in visit:
                return False
            
            visit.add(cNum)
            
            for prereq in preMap[cNum]:
                if not dfs(prereq):
                    return False
            
            visit.remove(cNum)
            preMap[cNum] = []
            return True
        
        # account for disconnected graph
        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True
