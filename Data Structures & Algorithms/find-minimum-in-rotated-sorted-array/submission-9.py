"""
nums = 

[1,2,3,4,5]: left
[5,1,2,3,4]: left
[4,5,1,2,3]: left, right
[3,4,5,1,2]
[2,3,4,5,1]
[1,2,3,4,5]

find smallest 

mid = nums[left] + nums[right] 
one var to get min
when do we go left? 
- mid > left and left < right
- mid  < left and left > right
when do we go right? 
- mid > left and left > right
- mid < left  and left < right

just right
[1,2,3,4,5]: left
[5,1,2,3,4]: left
[4,5,1,2,3]: left, right
[3,4,5,1,2]
[2,3,4,5,1]
[1,2,3,4,5]

mid < right -> go left
mid < right -> go left
mid < right -> go left = mid > right -> go right
mid > right -> go right
mid > right -> go right
mid < right -> go left

at the end just return num[l]?
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r)//2
           
            if (nums[mid] < nums[r]):
                # go left
                r = mid
            else:
                l = mid + 1
        return nums[l]
        