#want to buy --> cheapest
#sell --> most expensive
#sell date can't be less than buy date
#profit: sell - buy
#what if there is no good sell date? --> return 0
#edge case: all int? empty list? 
#time: O(n)
#space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #a variable to store max
        maxProfit = 0
        minBuy = float("inf")

        #iterate through the price list and consider each as selling price
        for i in range(len(prices)):
  

            #for each selling --> look left to see the smallest of it 
            if prices[i] < minBuy:
                minBuy = prices[i]

            #only consider sell-buy > 0
            profit = prices[i] - minBuy
            if profit > maxProfit:
                maxProfit = profit
        return maxProfit




        