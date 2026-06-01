class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        def robChoice(lst):
            one, two = 0,0
            res = 0
            for i in lst:
                res = max(two , one + i)
                one = two
                two = res
            return two
        return max(robChoice(nums[:-1]), robChoice(nums[1:]))
        