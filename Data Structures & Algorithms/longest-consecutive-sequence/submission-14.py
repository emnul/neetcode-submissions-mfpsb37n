class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # add each num to a set, the beginning of a seq will not have a left neighbor
        if not nums:
            return 0

        s = set(nums)
        res = 1
        for num in s:
            if num - 1 not in s:
                seq = 1
                tmp = num
                while tmp + 1 in s:
                    tmp += 1
                    seq += 1
                res = max(seq, res)
        return res