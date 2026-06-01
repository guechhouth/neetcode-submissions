'''
understand

s -> uppercase english chars
k -> int, can choose up to k chars to replace them with other upper eng char

perform at most k replacement 
-> return the length of the longest substring: has only 1 distinct char
"AAABABB" k = 1 -> "AAAAA" = 5

time:O(n), length of given string
space: O(m), num of unique char

'''
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dct = defaultdict(int)
        l = 0
        r= 0
        maxLen = 0

        while r < len(s):
            dct[s[r]] +=1
            if (r-l+1) - max(dct.values(), default=0) <= k:
                maxLen = max(maxLen, r-l+1)

            
            else:
                dct[s[l]] -= 1
                l+=1
            r+=1   

        return maxLen
# XYYX
# AAABABB, k = 1  , len = 7
#l = 0
#r= 0,1, 2,3,4
#charSet = [A,B,
#max = 5


        