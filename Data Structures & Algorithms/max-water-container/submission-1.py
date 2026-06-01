class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0,len(heights)-1
        maxWater = 0

        while l < r:
            #area = width x height
            water = (r-l) * min(heights[l], heights[r])
       
            #get max
            if water > maxWater:
                maxWater = water
            
            #move pointer at the shorter height 
            #this is the only way to increase the height
            if heights[l] <= heights[r]: 
                l += 1
            else:
                r -= 1
        return maxWater




        