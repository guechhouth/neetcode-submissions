class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        set 
        l = 0, r = 1, go until r < len(s)

        'zx' = 2, set= (z,x) r += 1
        y not in s 
        'zxy' = 3, set (z,x,y) r += 1
        z in set then we l += 1, set (x,y) -> (x,y,z) = 3
        r +=1
        '''
        seen = set()
        maxL = 0

        l, r = 0, 0
        
        while r < len(s):
            if s[r] in seen:
                while s[r] in seen:
                    
                    seen.remove(s[l])
                    l += 1
                    print(seen)
                    print(l)
            seen.add(s[r])
            maxL = max(maxL, r-l+1)
            r += 1
            print("r:", r)
        return maxL




        