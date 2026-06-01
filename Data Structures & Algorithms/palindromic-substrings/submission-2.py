'''
- to take into consideration when doing l-=1 and r+=1 => only get palindrome of odd
length so 'aa' will be missed
how to deal with it:
- palindrome of odd length --> same approach, L and R from same
- palindrome of even legngth --> start with L and R = L+1

'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        self.resCount = 0
        #integer is immutable in python, passing it in recursive call wont update 
        #the actual variable outside

        def palindrome(l,r):
            #this does not take into the consideration 'aaa' example 'aa'
            while l >= 0 and r < len(s) and s[l] == s[r]:
                
                self.resCount +=1
                l -= 1
                r +=1
            return
        
 
        for i in range(len(s)):
            #add one every time we call palindrom as single char isalso palindrome
            palindrome(i,i)
            palindrome(i,i+1)
    
        return self.resCount
        

        