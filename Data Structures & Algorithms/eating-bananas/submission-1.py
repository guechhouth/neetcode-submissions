"""
input: piles (arr), piles[i] = # bananas
        h: # of hours have to eat bananas

- decide k: # bananas/hour
- if a pile has less than k bananas, cannot proceed to new pile with
remaining time in that hour

output: min k such that can eat all bananas within h hours

approach: 
- binary search to find the min k, start with l = min # banana in the pile and r = max # of banana in the pile, k =  max, then cal mid = (l + r)/2 and assign to k if k is possible keep shrinking or expandng k
-- update min and max value of k until it converages to k
-- starting min = smallest piles[i]
-- start max = smallest piles[i]

- main loop going from left to right and add bananas for time h 
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # init k 
        low = 1
        high = k = max(piles)

        def feasible(mid):
                hours = 0
                for i in piles:
                        hours += math.ceil(i/mid)
                return (hours <= h)


        while low < high:
                mid = (high + low) // 2
                if feasible(mid):
                        # can go left, smaller k possible
                        high = mid
                else:
                        # go right
                        low = mid + 1 # need larger k
        return low





        