class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        cache = {}
        
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            
            rob = nums[i] + dfs(i+2)
            notRob = dfs(i+1)
            cache[i] = max(rob, notRob)
            return cache[i]
            
        return dfs(0)