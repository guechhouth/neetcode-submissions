'''
clarifying question: digits only group from left to right? or in any combination?
- left to right

4 cases to consider:
- group by digit: 
- 11
- 12
- 21
- 22
actually there are more case for odd
- 221
- 121
etc...

how to appraoch the problem
- draw decision tree
example: 1234
        
       /  \
      1   12
     / \  / \
    2  23 3  34
   / \
   3 34     

this is not efficient: 2^n
better? when take 1, how many ways to decode the remaining string: 234
- dimension of cache: N
- every time we go to a position i: we only have two decision to make: O(1)
=> overal O(n), O(n)
-> solving with actual dp: O(1) space
set dp of dp[i] = dp[i+1] + dp[1+2]. starting at 1, can take 2 or 23

'''
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1}

        def dfs(i):
            #base case 1: storing the results of the subproblem
            if i in dp:
                return dp[i]
            #base case 2
            if s[i] == "0":
                return 0
            
            res = dfs(i+1)
            if (i+1 < len(s) and ((s[i] == "1") or (s[i] == "2" and s[i+1] in "0123456"))):
                res += dfs(i+2)
            
            dp[i] = res
            return res
        
        return dfs(0)
        