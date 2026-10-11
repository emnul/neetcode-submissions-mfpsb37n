class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses # in[course] -> # of deps
        adjList = collections.defaultdict(list)

        # create adjList and calc indegree of all nodes
        for crs, pre in prerequisites:
            indegree[pre] += 1
            adjList[crs].append(pre)
        
        q = collections.deque()

        # add all courses w/ 0 deps to q
        for course, numDeps in enumerate(indegree):
            if numDeps == 0:
                q.append(course)

        finish = 0
        while q:
            for i in range(len(q)):
                course = q.popleft()
                finish += 1

                for neighbor in adjList[course]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)
        
        return numCourses == finish
                  


                
                
        
        
