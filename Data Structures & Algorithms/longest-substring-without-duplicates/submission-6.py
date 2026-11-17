class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        longest = 0
        l, r = 0, 0

        while r < len(s):
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[r])
            r += 1
            

            longest = max(longest, len(sub))

        return longest
