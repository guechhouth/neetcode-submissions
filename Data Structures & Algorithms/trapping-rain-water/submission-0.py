"""
only between the bar, bar-wall -> not counted
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        # brute force
        # edge cases
        if len(height) == 0 or not height:
            return 0
        
        total = 0
        # formula: min(height[l], height[r])  - height[i]
        for i in range(1, len(height) - 1):
            l = i - 1
            r = i + 1
            while l >= 0 and r < len(height):
                vol = min(height[l], height[r]) - height[i]
                print(f"vol: {vol}")
                if vol <= 0:
                    continue
                total += vol
                l -= 1
                r += 1
        return total
        """
        # cleverer solution
        # edge cases
        if len(height) == 0 or not height:
            return 0
        
        n = len(height)
        pre = [0] * n # max height from left of  i not including i
        suf = [0] * n # max height to the right of i not including i

        # prefix using prefix max - dp
        for i in range(1, len(height)):
            pre[i] = max(pre[i - 1], height[i-1]) #the element before
        # suffix using suffic max - dp
        for i in range(len(height) -2, -1, -1):
            suf[i] = max(suf[i + 1], height[i + 1])
            
        # iterate through the pre and suf and calcualte total water
        total = 0
        for i in range(n):
            water = min(pre[i], suf[i]) - height[i]
            if water > 0:
                total += water
        return total


        


             
        
        