class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        curr = set()
        actual = len(nums) + 1
        for i in nums:
            curr.add(i)
        for i in range(actual):
            if not curr:
                break
            if curr.pop() != i:
                return i
                break
        #the last element is not there
        return actual-1
        
        