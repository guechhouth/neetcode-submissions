'''
bottom up approach
best combinations to get 7 from [1,3,4,5]
DP[0] = 0  #base case
DP[1] = 1 
DP[2] = 2
DP[3] = 1
DP[4] = 1
DP[5] = 1
DP[6] = 2
DP[7] = (1) 1 + DP[6] = 3, (3) 1 + DP[4] =2, (4) 1 + DP[3] = 2, (5) 1+DP[2] =3
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)

        dp[0] = 0

        for amt in range(1, amount+1):
            for c in coins:
                if amt - c >= 0:
                    #dp[7] = 1 + DP[6] --> one possible solution
                    dp[amt] = min(dp[amt], 1 + dp[amt-c])
        return dp[amount] if dp[amount] != amount+1 else -1


        