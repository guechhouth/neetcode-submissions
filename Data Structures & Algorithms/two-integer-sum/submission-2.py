class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #method 1: brute force
     
        lst = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (j < len(nums)-1) and (nums[i] + nums[j] == target) and i != j:
                    lst += [i]
                    lst += [j]
                    return sorted(lst)
        

           
                    

        