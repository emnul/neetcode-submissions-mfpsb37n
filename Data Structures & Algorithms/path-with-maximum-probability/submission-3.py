class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjList = collections.defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            prob = succProb[i]
            adjList[src].append((dst, prob))
            adjList[dst].append((src, prob))
        
        maxProbs = collections.defaultdict(float) # node -> maxProb of success
        maxHeap = [(1.0, start_node)]

        while maxHeap:
            prob, node = heapq.heappop_max(maxHeap)

            if node == end_node:
                return prob

            if node not in maxProbs:
                maxProbs[node] = prob
            else:
                continue
            
            for nei, neiProb in adjList[node]:
                if nei not in maxProbs:
                    heapq.heappush_max(maxHeap, (neiProb * prob, nei))
        
        return maxProbs[end_node]




