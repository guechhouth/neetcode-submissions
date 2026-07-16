class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)

            res = 0
            length = len(str(n))
            while n > 0:
                res += (n % 10) ** 2
                n = n // 10
            n = res
            
        if n == 1:
            return True
        return False
                


        