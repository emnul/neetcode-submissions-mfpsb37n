from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if not nums:
            return False

        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        return max(list(counts.values())) > 1
