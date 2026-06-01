class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dct = {}
        for i in nums:
            dct[i] = 1 + dct.get(i,0)
        
        for k,v in dct.items():
            if v >= 2:
                return True
        return False
        