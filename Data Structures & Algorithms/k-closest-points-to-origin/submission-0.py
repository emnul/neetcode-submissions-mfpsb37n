import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.quickSort(points, 0, len(points) - 1)
        return points[:k]
    
    def quickSort(self, points, s, e):
        if e - s + 1 <= 1:
            return
        
        left = s
        pivot = points[e]

        for i in range(s, e):
            if self.dist(points[i]) < self.dist(pivot):
                points[left], points[i] = points[i], points[left]
                left += 1

        points[left], points[e] = points[e], points[left]

        self.quickSort(points, s, left - 1)
        self.quickSort(points, left + 1, e) 
    
    def dist(self, p):
        return math.sqrt((p[0] - 0) ** 2 + (p[1] - 0) ** 2)