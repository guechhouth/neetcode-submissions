'''
we have: number of zeros in front (n) = 32 - len("10101")

output: "10101" + 'n' = in range of 32

'''

class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        #convert the number into binary first because here it is not given as binary
        def convert(num):
            if num == 0:
                return "0"
            if num == 1:
                return "1"
            remain = num % 2
            return str(remain) + convert(num//2)
        

        #getting the thing
        string = int(convert(n))

        #calculation
        zeros = 32 - len(str(string))
        output = 0
              

        for i in range(zeros+1,33):
            num = string % 2
            output += num * (2**i)
            string = string >> 1
        return output
        '''
        res = 0

        for i in range(32):
            bit = (n>>i)&1
            res = res | (bit << (31-i))
        return res
        
            



        