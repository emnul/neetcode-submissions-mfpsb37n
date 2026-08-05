class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandToStud = collections.Counter(students)
        count = len(students)

        for s in sandwiches:
            if sandToStud[s] > 0:
                count -= 1
                sandToStud[s] -= 1
            elif sandToStud[s] == 0:
                break
        return count
