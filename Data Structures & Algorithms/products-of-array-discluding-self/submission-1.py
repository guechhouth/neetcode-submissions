class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #lst = [];

        '''
        for i in range(len(nums)):
            product = 1;
            for j in range(len(nums)):
                if nums[i] != nums[j]:
                    product *= nums[j]
            lst.append(product)
        return lst

        #time complexity: O(n^2), space complexity: O(1)
        '''

        '''
        solve in O(n)
        '''
        # total = 1
        # pointer1 = 0
        # pointer2 = 0
        # while pointer1 < len(nums):
        #     if (pointer2 == len(nums)):
        #         lst.append(total)
        #         pointer1 += 1
        #         total =1
        #         pointer2 = 0
        #         continue
        #     elif (pointer1 != pointer2):
        #         total *=nums[pointer2]
        #         pointer2 +=1
        #     elif (pointer2 < len(nums) or pointer1 == pointer2):
        #         pointer2 += 1
        # return lst

        # if len(nums) == 1:
        #     return [0]

        #assuming num len is >= 2 is valid
        output = [1] * len(nums)

        #going through the array the first time
        pre = 1
        for i in range(len(nums)):
            output[i] *= pre
            pre *= nums[i]
        
        pos = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= pos
            pos *= nums[i]
        
        return output

            


        




















        

        