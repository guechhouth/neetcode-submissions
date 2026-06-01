class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        curr = set(nums)
        actual = len(nums)
        
        for i in range(actual+1):
            if i not in curr:
                return i

        
        