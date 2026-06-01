class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s = 0, 1
        maxP = 0
        while s < len(prices):
            if prices[s] - prices[b] < 0:
                b = s
            else:
                maxP = max(maxP, prices[s] - prices[b]) 
                s += 1
        return maxP