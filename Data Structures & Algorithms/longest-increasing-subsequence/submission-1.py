'''
understand
- no change in relative order, increasing
- deleting some elements

e.g: [9,1,4,2,3,3,7]

'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [1] * len(nums)

        #go through the range, in reverse
        for i in range(len(nums)-1,-1,-1):
            #the last element
            if i == len(nums) -1:
                cache[i] = 1
            elif nums[i] == nums[i+1]:
                cache[i] = cache[i+1]
            elif nums[i] < nums[i+1]:
                if i+2 <= len(nums)-1 and nums[i+2] > nums[i]:
                    cache[i] = max(1, 1+cache[i+1], 1+cache[i+2])
                elif i+2 <= len(nums) -1 and nums[i+2] == nums[i]:
                    cache[i] = max(1,1+cache[i+1], cache[i+2])
                else:
                    cache[i] = max(1, 1+cache[i+1])
            elif nums[i] > nums[i+1]:
                for j in range(i, len(nums)):
                    if i == j:
                        cache[i] = 1
                    elif nums[i] > nums[j]:
                        continue
                    elif nums[i] < nums[j]:
                        if  j+1 <= len(nums)-1 and nums[j+1] > nums[i]:
                            cache[i] =max(1, 1 + cache[j], 1+ cache[j+1])
                        elif j+1 <= len(nums) -1 and nums[j+1] == nums[i]:
                            cache[i] = max(1,1+ cache[j], cache[j+1])
                        else:
                            cache[i] = max(1, 1+ cache[j])
                        break
        #finding the max in the cache
        return max(cache)

        '''
        most = []
        
        #run dfs on each number, and add posible combination into the list
        def dfs(num, index, longestStr, numLst):
            #base case, when it reaches the end
            maxLarge = num
            for i in numLst:
                if i > maxLarge:


        #looping through each numebr
        for i in range(len(nums)):
            tmp = nums
            dfs(nums[i],i, "", tmp[i:])
        
        return max(most)
        '''
        

        