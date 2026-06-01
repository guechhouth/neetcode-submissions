class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1:
            return []
        hmap = {}
        for i in nums:
            hmap[i] = target - i
        
        i1 = 0
        i2 = 0
        for k,v in hmap.items():
            if k in hmap.values():
                i1 = v
                i2 = k
        idx1 = -1
        counter = 0
        for i in range(len(nums)):
            if nums[i] == i1:
                idx1 = i
                i1 = i
                counter += 1
            if nums[i] == i2 and idx1 != i:
                i2 = i
                counter += 1
            if counter == 2:
                break



        if i1 <= i2:
            return [i1,i2]
        else:
            return [i2, i1]

        