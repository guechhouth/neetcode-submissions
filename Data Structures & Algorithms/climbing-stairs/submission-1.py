
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        #let a and b be the non-existent pointer 
        one, two = 1,1
        for i in range(n-1):
            tmp = one + two
            one = two
            two = tmp
        return two

        
        