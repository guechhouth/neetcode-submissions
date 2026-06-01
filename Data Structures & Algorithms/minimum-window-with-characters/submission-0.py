'''understand
string s
string t

shortest substring in s such that every char in t (duplicate) is in the substring

does not exist --> empty string

#left = first char in t that is in substring
#right = incremented
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #base 
        if s == t:
            return s
        if len(s) < len(t):
            return ""
        countT, window = {},{}
        res, resLen = "", float('inf')
        l = 0
        
        for i in t:
            countT[i] = 1 + countT.get(i,0)
    
        have, need = 0, len(countT)
        
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r],0)

            if s[r] in countT and window[s[r]] == countT[s[r]] :
                have += 1
            while have == need:
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    res = s[l:r+1]
                window[s[l]] -=1
                if (s[l] in countT) and window[s[l]] < countT[s[l]]:
                    have -= 1
                    
                l+=1
                
        return res
            



        