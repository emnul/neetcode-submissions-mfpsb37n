class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        hmStud = collections.Counter(students)
        studs = collections.deque(students)
        sands = collections.deque(sandwiches)

        while sands and hmStud[sands[0]] > 0:
            if studs[0] != sands[0]:
                cur = studs.popleft()
                studs.append(cur)
            else:
                hmStud[sands[0]] -= 1
                studs.popleft()
                sands.popleft()
        
        return len(studs)