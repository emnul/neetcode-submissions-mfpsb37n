class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = collections.defaultdict(list)
        for src, dst in edges:
            adjList[src].append(dst)
        
        def dfs(node, curPath):
            # detect bad dst
            if not adjList[node] and node != destination:
                return False
            # detect cycle
            if node in curPath:
                return False
            
            curPath.add(node)
            for nei in adjList[node]:
                if not dfs(nei, curPath): return False
            curPath.remove(node)
            
            return True

        return dfs(source, set())