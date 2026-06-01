class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        [1,7,2,5,4,7,3,6]
        - (7-0) * 1 = 7
        1 < 6 -> l += 1, at l we have 7
        - (7 - 1) * 6 = 36 , new kmax is 36
        r -= 1, r at index 6
        

        '''
        l, r =0, len(heights) -1
        maxWater = 0

        while l < r:
            w = r - l
            h = min (heights[l],heights[r])
            maxWater = max(w*h, maxWater)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxWater


        