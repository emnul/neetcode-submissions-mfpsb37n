class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for i in range(len(nums)):
            count = 0
            if nums[i] - 1 not in s:
                seqStart = nums[i]
                while seqStart in s:
                    count += 1
                    seqStart += 1
                longest = max(longest, count)
        return longest
