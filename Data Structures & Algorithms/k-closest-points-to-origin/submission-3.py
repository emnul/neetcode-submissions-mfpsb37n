class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(p):
            return p[0] ** 2 + p[1] ** 2

        def partition(l, r):
            pivotIdx = r
            pivotDist = dist(points[pivotIdx])

            i = l
            for j in range(l,r):
                if dist(points[j]) <= pivotDist:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            
            points[i], points[r] = points[r], points[i]
            return i

        l,r = 0, len(points) - 1
        pivot = len(points)

        while pivot != k:
            pivot = partition(l, r)
            if pivot < k:
                l = pivot + 1
            else:
                r = pivot - 1
        return points[:k]



        

    
    