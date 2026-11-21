class Solution:
    def climbStairs(self, n: int) -> int:
        step_1, step_2 = 1, 1

        for i in range(1, n):
            total = step_1 + step_2
            step_2 = step_1
            step_1 = total
        return step_1
