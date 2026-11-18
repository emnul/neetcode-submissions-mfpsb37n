class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        
        dp = [0, 1]

        i = 1
        while i <= n:
            tmp = dp[0]
            dp[0] = dp[1]
            dp[1] = tmp + dp[1]
            i += 1
        
        return dp[1]
        