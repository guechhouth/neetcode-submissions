class Solution:
    def isPalindrome(self, s: str) -> bool:
        #initialize two pointers, one to keep track of char forward, the other is for backward
        p1 = 0
        p2 = len(s) -1

        while p1 < p2:
            
            if not s[p1].isalnum():
                p1 += 1
                continue
            if not s[p2].isalnum():
                p2 -= 1
                continue
            if s[p1].lower() == s[p2].lower():
                p1 += 1
                p2 -= 1
            else:
                return False
        return True
            

        