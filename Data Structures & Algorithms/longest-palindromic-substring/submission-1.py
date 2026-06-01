class Solution:
    def longestPalindrome(self, s: str) -> str:
        #max variable to store all the combination
        res = []
        def palindrome(l,r, word):
            if l < 0 or r >= len(s) or s[l] != s[r]:
                #reach the end
                res.append(word)
                return
            if s[l] == s[r]:
                palindrome(l-1,r+1, s[l]+word+s[r])
            return
            
        for odd in range(len(s)):
            palindrome(odd-1,odd+1, s[odd])
        for even in range(len(s)):
            palindrome(even, even+1, '')
        
        length = 0
        for w in res:
            if length < len(w):
                longest = w
                length = len(w)
        return longest
        