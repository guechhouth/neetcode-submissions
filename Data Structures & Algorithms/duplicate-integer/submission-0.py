class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create dictionary
        dct = {}
        for num in nums:
            if num not in dct:
                dct[num] = 1
            else:
                dct[num] += 1
        for num,k in dct.items():
            if k > 1:
                return True
        return False
         