class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = collections.defaultdict(list)
        for src, dst in edges:
            adjList[src].append(dst)
        
        states = [0] * n

        def backtrack(node):
            # dupe detect
            if states[node] == 1:
                return False
            # detect dest
            if states[node] == 2:
                return True
            if not adjList[node]:
                return node == destination
            
            states[node] = 1
            for nei in adjList[node]:
                if not backtrack(nei): return False

            states[node] = 2
            return True




        return backtrack(source)
