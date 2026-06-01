class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxLength = float('-inf')
        prevMax = 0
        for i in range(len(nums)):
            prevMax = max(nums[i], prevMax + nums[i])
            maxLength = max(prevMax, maxLength)
        return maxLength

        