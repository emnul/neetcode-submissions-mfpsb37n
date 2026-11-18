class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = collections.defaultdict(int)
        
        def memo(i):
            if i >= len(nums):
                return 0
            if cache[i] > 0:
                return cache[i]
            
            cache[i] = max(nums[i] + memo(i + 2), memo(i + 1))
            return cache[i]

        return memo(0)