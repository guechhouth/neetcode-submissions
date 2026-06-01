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
        mapT = {i: 0 for i in range(26)}
        mapS = {i: 0 for i in range(26)}
     
        for i in t:
            i = i.lower()
            mapT[ord(i) - ord("a")] = 1 + mapT.get(ord(i)-ord("a"), 0) 
        for j in s:
            j = j.lower()
            mapS[ord(j) - ord("a")] = 1 + mapS.get(ord(j)-ord("a"), 0) 
        
        return mapS == mapT
        