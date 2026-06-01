'''
nums[i] = max jump length 
- can choose to jump at that or not

- draw decision tree using the node as index 

- DP approach- cache: we can use dp[index] = False = can't
--> O(n^2) 

- Greedy approach: starting from the goal

[2,3,1,1,4]
- consider [1,4] --> can reach
- now goal is 1: consider [1,1] --> can reach again
- now goal is 1: consider [3,1] --> again
- now goal is 3: consider [2,3] --> again

[1,3,0,0]
[_, goal]
- consider [0,0] --> no
- consider [3,0] --> yes
- now goal is 3: consider [1,3] --> yes
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) -1
        for i in range(len(nums) -1, -1, -1):
            if i + nums[i] >= goal:
                #can reach
                goal = i
            #we dont update the goal
        return True if goal == 0 else False

            


        