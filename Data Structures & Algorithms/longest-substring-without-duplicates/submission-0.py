class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        longest = 0

        l, r = 0, 0
        length = 0
        while r < len(s):
            if s[r] not in window:
                window.add(s[r])
                length += 1
                longest = max(length, longest)
                r += 1
            else:
                window.remove(s[l])
                length -= 1
                l += 1
        return longest