'''
return the length of the longest common subsequencne between 2 strings 

return 0 if one exists and other does not 

- no change in sequence: we can go left to right of right to left

- edge case:
1. what happen when one string is empty ? return 0
2. what happen in this case: ca, cb ? so c is the answer --> maxLegnth = 1

- approach:
-- we go through the longest string
-- using dp at each index
-- at each index we store the max length so far until this index
----- so we iterate through the longest string once
----- but every time, we check from the beginning of the shorter string 
|______ so this is not efficient 


use 2d approach
one is on each axis
use bottom up approach 
- match --> we go diagonal up
- does not match --> we go either down or right and take max


'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1)+ 1)] #at least another column for 0s

        for i in range(len(text1) -1, -1, -1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        print(dp)
        return dp[0][0]

        


            










        