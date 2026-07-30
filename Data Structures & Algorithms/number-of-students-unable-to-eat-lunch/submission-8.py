class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = collections.Counter(students)
        res = len(students)

        for s in sandwiches:
            if counts[s] > 0:
                counts[s] -= 1
                res -= 1
            else:
                return res
     
        return res