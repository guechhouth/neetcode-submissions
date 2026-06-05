class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        if not matrix:
            return False
        
        # x-axis
        x_min = 0
        x_max = len(matrix) - 1
        # y-axis
        y_min = 0
        y_max = len(maxtrix[0]) - 1

        while x_min < x_max and y_min < y_max:
            mid_x = (x_min + x_max)//2
            mid_y = (y_min + y_max)//2

            if target == matrix[mid_x][mid_y]:
                return True
            elif target < matrix[mid_x][mid_y]:
                # can either go left same row or go up
                
            else:
                # can either go right same row or go down
        """
        arr = []
        # convert to 1 D
        for l in matrix:
            for i in l:
                arr.append(i)
        
        l = 0
        r = len(arr) - 1
        while l <= r:
            m = (l + r)//2
            if target == arr[m]:
                return True
            elif target < arr[m]:
                r = m -1
            else:
                l = m + 1
        return False


        