"""
n = 4
_ _ _ _
dp = max number of distinct ways from this to end 

dp[n]

dp[4] = 1
dp[3] = 1
dp[2] = jump 2 steps directly or (1+1) = 2
dp[1] = dp[2] + dp[3]



dp[i] = max(1+dp[i-1], )
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        one = 0
        two = 1
        for i in range(n):
            temp = one
            one = two
            two = temp + two
        return two

        