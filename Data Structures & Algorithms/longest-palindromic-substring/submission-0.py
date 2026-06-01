'''
brute force: take each substring from a particular char and check for palindrome
- time complexity is N.N^2 = N^3
--> N^2: generate all possible substring
--> N: for checking palindrome

a better approach: expanding outward instead
For each character (and between characters) in the string, 
treat it as the center of a potential palindrome.

Expand outward left and right while characters match.

Each expansion step checks palindrome validity in O(1) time 
per step because you compare just the new pair of characters.

You repeat this for each center.

-time complexity: NxN
--> N for traversing
--> N for checking palindrome
N centers to check

Each center expands up to N times

So total: O(N²), which is faster than brute force O(N³)


'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        def dfs(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return l+1,r-1

        res = ""
        resLen = 0
        for c in range(len(s)):
            #for odd
            lOdd, rOdd = dfs(c,c)
            odd = s[lOdd:rOdd+1]
            if resLen < len(odd):
                resLen = len(odd)
                res = odd
            #for even
            lEven, rEven = dfs(c,c+1)
            even = s[lEven:rEven+1]
            if resLen < len(even):
                resLen = len(even)
                res = even
            
            
        return res

        