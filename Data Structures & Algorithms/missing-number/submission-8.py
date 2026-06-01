class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        #O(n) time and space
        curr = set(nums)
        actual = len(nums)
        
        for i in range(actual+1):
            if i not in curr:
                return i
        '''
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        return res

        
        