class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            # check if num is start of a seq
            if num - 1 not in numSet:
                tmp = num
                seqLen = 0
                while tmp in numSet:
                    seqLen += 1
                    tmp += 1
                longest = max(longest, seqLen)

        return longest
