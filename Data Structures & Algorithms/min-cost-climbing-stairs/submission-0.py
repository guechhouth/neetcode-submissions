"""
input: 
- arr -> cost: cost[i] = cost of taking a step from the ith floor of a staircase

rule: 
- choice: (i + 1)th or (i+2)th step after paying cost[i]
- can start at index 0 or 1

want:
min cost to reach top of the staircase -> pass the last index cost

cost at i = min(cost[i] + cost[i-1], cost[i] + cost[i-2])
one = 0, two = 0
[1,2,1,2,1,1,1] -> cost
[1,2,2,4,3,4,4]
cost[0] = 1
cost[1] = min(2+1, 2) = 2
cost[2] = min(1+2, 1+1) = 2
cost[3] = min(2+2, 2+2) = 4
cost[4] = min(4+ 1, 2+1) = 3
cost[5] = min(3+ 1, 4+1) = 4
cost[6] = min(4+1, 3+1) = 4


"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one_back = 0
        two_back = 0
        min_cost = 0
        i = 0
        while i < len(cost) + 1:
            if i == len(cost):
                temp_cost = two_back
                min_cost = min(min_cost, temp_cost)
            else:
                min_cost = min(cost[i] + one_back, cost[i] + two_back)
                temp = one_back
                one_back = min_cost
                two_back = temp
            i += 1
        return min_cost        


        