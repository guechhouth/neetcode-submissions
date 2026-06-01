'''
curr = [1,2,4,6]

at 1: 2*4*6
at 2: 1*4*6
at 4: 1*2*6
at 6: 1*2*3

res = [1,1,1,1]
going from front: 
- 1 -> res[0] * curr[1]
- 2 -> res[1] * curr[2]
- 3 -> res[2] * curr[3]
--> [2,4,6,1]


'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        res = [1] * len(nums)

        #going forward
        prevF = 1
        for i in range(len(nums)):
            if i == 0:
                tmp = prevF
                prevF = nums[i]
                res[i] = 1 * tmp
            
            else:
                tmp = prevF
                prevF = nums[i]
                res[i] = res[i-1] * tmp
        print(res)
        
        #going backward
        prevB = 1
        for i in range(len(nums)-1,-1,-1):
            #[1,1,2,8]
            #[1,2,4,6]
            if i == len(nums)-1:
                tmp = prevB
                prevB *= nums[i]
                res[i] *=  1 * tmp
            else:
                tmp = prevB
                prevB *= nums[i]
                res[i] *=  tmp
        return res

                

        