class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we can find the length of the longest substring using a set and
        # the sliding window technique. we use a left and right pointer to
        # track the beginning of the substring. we add the element that the
        # right pointer is pointing at if it's not already in the set
        # if the element at the right pointer is already in the set we
        # increment the left pointer / shrink the window until the element is
        # no longer in the set

        substr = set()
        longest = 0
        l = 0
        for r in range(len(s)):
            while s[r] in substr:
                substr.remove(s[l])
                l += 1
            
            substr.add(s[r])
            longest = max(longest, len(substr))

        return longest