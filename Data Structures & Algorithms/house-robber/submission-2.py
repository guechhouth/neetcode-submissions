"""
nums = [1,1,3,3]
cannot rob two adjacent house
max amount of money you can rob

dp = max amount of money you can rob once you reach this house

Input: nums = [2,9,8,3,6]

dp[i] = max(dp[i-1], num[i] + dp[i-2])

[0,0,2,9,10,12,16]

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 2)

        for i in range(len(nums)):
            dp[i+2] = max(dp[i+1], nums[i] + dp[i])
        
        return dp[-1]
        