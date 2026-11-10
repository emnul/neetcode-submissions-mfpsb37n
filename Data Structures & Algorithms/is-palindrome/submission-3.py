class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s = s.lower()

        while l < r:
            # ensure l is valid ascii char
            while l < r and not s[l].isalnum():
                l += 1
    
            # ensure r is valid ascii char
            while l < r and not s[r].isalnum():
                r -= 1

            # both chars are valid, compare
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1
        
        return True

            
            
