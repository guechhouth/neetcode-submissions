class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        one, two = 0, 0
        res = 0
        for i in range(len(nums)):
            res = max(two, one + nums[i])
            one = two
            two = res
        return two

            



        