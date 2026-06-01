class Solution:
    def countBits(self, n: int) -> List[int]:
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

             
        