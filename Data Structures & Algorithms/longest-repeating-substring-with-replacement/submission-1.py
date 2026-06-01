from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        s = "XYYX"
        k = 2
        k = 1:
        max = 1
        {
            X : 1

        }
        '''
        fMap = defaultdict(int)
        l = 0
        res = 0
        curC = s[l]


        for r in range(len(s)):
            
            fMap[s[r]] = 1 + fMap.get(s[r], 0)

            while (r - l + 1) - max(fMap.values()) > k:
                fMap[s[l]] -= 1
                l += 1
            res = max(res, r -l + 1)


        return res
            
                
                

        