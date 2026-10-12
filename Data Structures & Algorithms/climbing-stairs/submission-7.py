class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def dp(step):
            if step in cache:
                return cache[step]
            if step == n:
                return 1
            if step > n:
                return 0
            
            cache[step] = dp(step + 1) + dp(step + 2)

            return cache[step]
        
        return dp(0)
            