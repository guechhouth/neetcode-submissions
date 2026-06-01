class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #visited set to check if the number is visited and backtrack?
        #set to store result and check if a combination alr exists?
        visit = []
        #recurisive here
        def backtrack(i, lst,total):
            #using index to keep track of when to check number
            if total == target:
                visit.append(lst.copy())
                return
            if i >= len(nums) or total > target:
                return

            #keep going with same number
            lst.append(nums[i])
            backtrack(i, lst, total+ nums[i])
            lst.pop()
            backtrack(i+1, lst,total)

        backtrack(0, [],0)

        return visit
        


        