from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        s = set(nums)
        for num in nums:
            # beginning of a seq
            if num - 1 not in s:
                length = 1
                curr = num
                while curr + 1 in s:
                    length += 1
                    curr += 1
                longest = max(length, longest)
            
        return longest
            

