class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        hm = {}

        for num in s:
            if num - 1 not in s:
                hm[num] = 1
                nextNum = num + 1
                while nextNum in s:
                    hm[num] += 1
                    nextNum += 1
        if len(hm.values()) > 0:
            return max(list(hm.values()))
        else: return 0