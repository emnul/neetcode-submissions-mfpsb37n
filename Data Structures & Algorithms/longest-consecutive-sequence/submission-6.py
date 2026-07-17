class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for num in s:
            if num - 1 not in s:
                length = 1
                nextNum = num + 1
                while nextNum in s:
                    length += 1
                    nextNum += 1
                longest = max(longest, length)
        return longest
        