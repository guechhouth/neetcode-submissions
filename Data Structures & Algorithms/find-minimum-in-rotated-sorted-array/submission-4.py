'''
array 
len(array) = n
rotated between 1-n times

all element are unque

return min in the array in O(logN) time

#construct a binary tree 

#since the array given i can just construct in that order

#apply search algo and try to find the left most of the left subtree, if left child
#else print out the val of the root, if tree not null

'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) ==0:
            return None
        #binary search
        minVal = float('inf')

        l, r = 0, len(nums) -1
        while l <= r:
            
            if nums[l] < nums[r]:
                minVal = min(minVal, nums[l])
                break
            mid = (l+r)//2
            minVal = min(minVal, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid+1
            else:
                r = mid-1
                #search left
        return minVal
'''#[4,5,6,7]
l = 0
r = 1 -> 0
mid = 1 (5), 0 (4)    
minVal = 5 -> 4 

[3,4,5,6,1,2]
l = 3
r = 5
mid = 2 (5) -> 4 (4)    
minVal = 5 -> 4 
'''


        