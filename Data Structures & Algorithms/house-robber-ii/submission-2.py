class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        def option(num):
            one, two = 0,0
            for i in num:
                curMax = max(one+i,two)
                one = two
                two  = curMax
            return two
        return max(option(nums[:-1]), option(nums[1:]))