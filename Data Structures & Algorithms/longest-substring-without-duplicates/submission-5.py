class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        longest = 0
        l = 0
        for r in range(len(s)):
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[r])
            longest = max(longest, r - l + 1)
        return longest