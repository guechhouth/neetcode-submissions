class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        distinct = {}
        l = r = 0
        max_length = 0
        while r < len(s):

            if s[r] not in distinct or distinct[s[r]] == 0:
                distinct[s[r]] = 1
                max_length = max(max_length, r - l + 1)
                r += 1
            
            else:
                while l < len(s) and distinct[s[r]] > 0:
                    distinct[s[l]] -= 1
                    l += 1
                    
                distinct[s[r]] += 1
                if r <= len(s) - 1 and l <= r:
                    max_length = max(max_length, r - l + 1)
                    r += 1
        return max_length
                


        