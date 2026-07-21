class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        longest = 0

        l, r = 0, 0
        while r < len(s):
            if s[r] not in window:
                window.add(s[r])
                longest = max(longest, len(window))
                r += 1
            else:
                window.remove(s[l])
                l += 1
        return longest