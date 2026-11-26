class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = collections.defaultdict(list)
        for src, dst, w in times:
            adjList[src].append((dst, w))

        minTimes = {}
        minHeap = [(0, k)]

        while minHeap and n > 0:
            w, node = heapq.heappop(minHeap)

            if node not in minTimes:
                minTimes[node] = w
                n -= 1
            else:
                continue

            for nei, wei in adjList[node]:
                heapq.heappush(minHeap, (wei + w, nei))
        
        return max(minTimes.values()) if n == 0 else -1
        

            