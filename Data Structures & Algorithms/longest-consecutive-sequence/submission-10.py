class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        [2,20,4,10,3,4,5]
        #set (2,20, 4,10, 3, 5)
        2 - 2-1? no
        20 - 20-1? no
        4 - 4 -1 ? yes
        10 -1 ? no
        3 - 1? yes
        5 - 4? yes


        '''
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        nums.sort()
        print(nums)

        maxLen =  float("-inf")
        currMax = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                maxLen = max(currMax, maxLen)
                continue
            if nums[i] == nums[i-1] + 1:
                currMax += 1
            if nums[i] != nums[i-1] + 1 or i == len(nums) -1:
                maxLen = max(currMax, maxLen)
                print(maxLen)
                currMax = 1
        return maxLen
                

        