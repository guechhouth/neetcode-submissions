"""
[4,5,6]
target = 10
{
4: 0
5: 1
6: 4

}
4: 10-4 = 6
5: 10 - 5 = 5
6: 10 - 6 = 4

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in hmap:
                hmap[nums[i]] = i
            else:
                min_num = min(hmap[diff], i)
                if min_num == hmap[diff]:
                    max_num = i
                else:
                    max_num = hmap[i]
                return [min_num, max_num] 
        return []

        