'''
Maintain four boundaries:
top = 0
bottom = m - 1
left = 0
right = n - 1

While top <= bottom and left <= right:
Traverse left → right across top, then top += 1.
Traverse top → bottom along right, then right -= 1.
Traverse right → left across bottom (if top <= bottom), then bottom -= 1.
Traverse bottom → top along left (if left <= right), then left += 1.
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0]) #right is num of col + 1
        top, bottom = 0, len(matrix) # number of row + 1

        while left < right and top < bottom:
            #get every i in the top row
            for i in range(left, right): #reaon for setting right of bound
                res.append(matrix[top][i])
                #update top variable, shift top down by 1
            top += 1

            #get every i in the right col
            for i in range(top, bottom):
                res.append(matrix[i][right -1]) #right is out of bound
            right -= 1 #shift to the left
            
            #why here
            if not (left < right and top < bottom):
                break

            #get every i in bottom: right to left
            for i in range(right-1, left-1, -1): #left is none inclusive
                res.append(matrix[bottom-1][i]) #bottom is also out of bound by 1
            bottom -= 1 #shift up
            #get every i in left most column
            for i in range(bottom -1, top -1, -1):
                res.append(matrix[i][left])
            left += 1


        return res






