from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        dstu = deque(students)
        dsand = deque(sandwiches)
        while dstu:
            # student at front of line likes sand
            if dsand[0] == dstu[0]:
                dstu.popleft()
                dsand.popleft()
            # no students want to eat sand at top of stack
            elif dsand[0] not in dstu:
                break
            else:
                # student moves to back of line since they dont like sand
                s = dstu.popleft()
                dstu.append(s)


        return len(dstu)