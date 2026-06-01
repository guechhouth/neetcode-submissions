class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        if not s and not t:
            return True
        if (s and not t) or (t and not s):
            return False
        else:
            return sorted(s) == sorted(t)
        #sort create new list so O(N) space
        '''
        if len(s) != len(t):
            return False
        mapT = {i: 0 for i in range(26)}
        mapS = {i: 0 for i in range(26)}
     
        for i in t:
            i = i.lower()
            mapT[ord(i) - ord("a")] += 1 
        for j in s:
            j = j.lower()
            mapS[ord(j) - ord("a")] += 1 
        
        return mapS == mapT
        