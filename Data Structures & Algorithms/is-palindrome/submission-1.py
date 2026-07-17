class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1
        s = s.lower()
        while L < R:
            print(s[L], s[R])
            print(L, R)
            if (
                (ord(s[L]) not in range(ord('a'), ord('z') + 1)) and 
                (ord(s[L]) not in range(ord('0'), ord('9') + 1))
            ):
               L += 1
               continue
            if (
                (ord(s[R]) not in range(ord('a'), ord('z') + 1)) and 
                (ord(s[R]) not in range(ord('0'), ord('9') + 1))
            ):
               R -= 1
               continue
            
            if s[L] != s[R]:
                return False
            
            L += 1
            R -= 1
        return True