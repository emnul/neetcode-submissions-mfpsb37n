class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = collections.defaultdict(list)
        for src, dst, w in times:
            adjList[src].append((dst, w))
        
        minTimes = {}
        minHeap = [(0, k)]

        while minHeap:
            w, node = heapq.heappop(minHeap)

            if node not in minTimes:
                minTimes[node] = w
            else:
                continue
            
            for nei, wei in adjList[node]:
                heapq.heappush(minHeap, (wei + w, nei))
        
        minTime = 0
        for node in range(1, n+1):
            if node not in minTimes:
                return -1
            else:
                minTime = max(minTime, minTimes[node])
        return minTime

            
            