class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0] * (n+1)
        for i in range(n+1):
            idx = i
            count = 0
            while i:
                if i & 1 == 1:
                    count += 1  
                i = i >> 1
          
            bits[idx] = count
        
        return bits


                

        