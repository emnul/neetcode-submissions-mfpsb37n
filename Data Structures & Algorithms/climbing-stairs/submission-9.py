class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # dp[0] = 1 step, dp[1] = 2 steps
        dp = [1, 1] # base case, size 2 because we only need prev 2 
        i = 0
        while i < n - 1:
            tmp = dp[0]
            dp[0] = dp[0] + dp[1] # sum of prev two becomes new prev
            dp[1] = tmp # old prev moves to 2nd prev
            i += 1
        
        return dp[0]