class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_points = [((point[0] ** 2 + point[1] ** 2 ) ,point) for point in points]
        heapq.heapify(dist_points)
        res = []

        for _ in range(k):
            res.append(heapq.heappop(dist_points)[1])
        return res