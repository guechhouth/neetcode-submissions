class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        #time complexity: O(nlogn), divide by two is log n and go through n times
        #space complexity: O(n)
        numlist = [0] * (n+1)

        def countOne(num, count):
            if num == 0:
                return count
            elif num == 1:
                count += 1
                return count
            elif num % 2 == 1:
                count += 1
            return countOne(num//2, count)
        for i in range(n+1):
            numlist[i] = countOne(i,0)
        return numlist
        '''

        #more efficient = = dynamic programming
        dp = [0] * (n+1)
        offset = 1
        
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i-offset]
        return dp


             
        