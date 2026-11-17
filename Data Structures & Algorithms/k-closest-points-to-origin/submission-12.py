class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distFromOrigin = point[0] ** 2 + point[1] ** 2
            heapq.heappush(heap, (-distFromOrigin, point))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return list(map(lambda tupl: tupl[1], heap))