"""
input: 
- arr: positive nums

wants:
- true -> partition arr into two subsets -> subset1 and subset2: sum(subset1) == sum(subset2)

eg: 
[1,2,3,4]
1+ 2+3+4 = 10
10/2 = 5

sum = [true,false,false,false,true, false]. 
        0,   1,    2,   3,    4,      5
1: 1
2: 2
3: 1+2, 3
4: 4
5: 


[t,f,t,f,f,f,f]
 0,1,2,3,4,5,6
6: 
6-2 = 4 = f
5-2 = 3 = f
4-2 = 2 = f
3-2 = 1 = f
2-2 = 0 = t
1-2 =

"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 != 0: # not possible if the total sum is not even
            return False 
        half = total // 2
        dp = [False] * (half +1)
        dp[0] = True

        for n in nums:
            for i in range(half, -1, -1): # starting from the back to avoid duplicate
                if (i - n) < 0:
                    continue # don't allow negative index, will mess up the array
                if dp[i - n] == True:
                    dp[i] = True
        print(f"{dp}")
        return True if dp[-1] == True else False
        


        