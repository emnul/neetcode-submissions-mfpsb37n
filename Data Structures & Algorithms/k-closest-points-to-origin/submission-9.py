class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        self.quickSort(points, 0, len(points) - 1, k)
        return points[:k]
    
    def quickSort(self, points, s, e, k):
        if e - s + 1 <= 1:
            return 
        pivotVal = self.dist(points[e])
        left = s

        for i in range(s, e):
            if self.dist(points[i]) <  pivotVal:
                points[left], points[i] = points[i], points[left]
                left += 1
        
        points[left], points[e] = points[e], points[left]
        
        if left == k:
            return
        
        self.quickSort(points, s, left - 1, k)
        self.quickSort(points, left + 1, e, k)

        

    def dist(self, p):
        return p[0] ** 2 + p[1] ** 2
