class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(p):
            return p[0] ** 2 + p[1] ** 2
        
        def partition(l, r):
            # todo implement quick sort
            pivotIdx = r
            pivotDist = dist(points[pivotIdx])

            pivot = l
            for i in range(l, r):
                if dist(points[i]) <= pivotDist:
                    points[pivot], points[i] = points[i], points[pivot]
                    pivot += 1
            points[pivot], points[r] = points[r], points[pivot]
            return pivot

        
        l,r = 0, len(points) - 1
        pivot = len(points)

        while pivot != k:
            pivot = partition(l, r)
            if pivot < k:
                l = pivot + 1
            else:
                r = pivot - 1
        return points[:k]
