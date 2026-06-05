class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                # go left 
                r = mid - 1
            else:
                # go right
                l = mid + 1
        return -1

        