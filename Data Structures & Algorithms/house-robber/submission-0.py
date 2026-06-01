class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0,0

        for i in range(len(nums)):
            curMax = max(one+nums[i],two)
            one = two
            two  = curMax
        return two        