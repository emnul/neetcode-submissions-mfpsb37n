class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = collections.defaultdict(list)
        for src, dst in edges:
            adjList[src].append(dst)
        
        states = [0] * n
        
        def dfs(node):
            # detect bad dst
            if not adjList[node] and node != destination:
                return False
            # detect cycle
            if states[node] == 1:
                return False
            # we've already explored this valid path
            if states[node] == 2:
                return True
            
            # exploring this node, put in pending state
            states[node] = 1
            for nei in adjList[node]:
                if not dfs(nei): return False
            states[node] = 2
            
            return True

        return dfs(source)