from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = {}
        for num in nums:
            if num in c:
                return True
            else:
                c[num] = 1
        return False
        