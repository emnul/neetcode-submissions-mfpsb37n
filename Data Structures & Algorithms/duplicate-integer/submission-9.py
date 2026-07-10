class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # duplicates are in array if set of nums contains
        # fewer values than nums array
        return len(set(nums)) < len(nums)