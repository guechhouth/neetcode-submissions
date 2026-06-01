
class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        if n == 0:
            return 0
        #let a and b be the non-existent pointer 
        one, two = 1,1
        for i in range(n-1):
            tmp = one + two
            one = two
            two = tmp
        return two
        '''
        cache = [-1] * (n)
        def dfs(i):
            if i >= n:
                return i==n
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i+1) + dfs(i+2)
            return cache[i]
        return dfs(0)

        
        