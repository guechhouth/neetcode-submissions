'''
understand
- finding a substring (contiguous string) that has no duplicate
- return the length of that string
- any duplicate
- all string valid 
- O(n) time and O(m) space

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
       
        #initialize two pointers
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res
        