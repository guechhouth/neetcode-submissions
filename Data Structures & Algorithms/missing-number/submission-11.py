class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #exclusive or the same number will be 0
        # the order does not matter 5^5^3 is just 3, 0^x = x

        res = len(nums) #also want to add n values

        for i in range(len(nums)):
            res += (i - nums[i]) #from 0 to len -1
        return  res

            
        