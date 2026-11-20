class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = collections.defaultdict(list)
        for src, dst in edges:
            adjList[src].append(dst)
        
        states = [0] * n

        def dfs(root):
            # found cycle
            if states[root] == 1:
                return False
            # already processed node
            if states[root] == 2:
                return True
            # at leaf node, but it's not destination
            if adjList[root] == [] and root != destination:
                return False
            
            states[root] = 1
            for nei in adjList[root]:
                if not dfs(nei): return False
            states[root] = 2
            return True


        return dfs(source)

