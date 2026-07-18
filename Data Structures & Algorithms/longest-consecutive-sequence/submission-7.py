class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # start of a sequence will not have number before it
        s = set(nums)
        longest = 0
        for i in range(len(nums)):
            # Found sequence start
            if nums[i] - 1 not in s:
                seqLen = 0
                curr = nums[i]
                while curr in s:
                    curr += 1
                    seqLen += 1
                longest = max(seqLen, longest)
        return longest
                
