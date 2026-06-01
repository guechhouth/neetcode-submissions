'''
return the number of intervals to be removed from the the list so that there is no
overlapping

- [1,2] and [2,3] does not overlap
- is the array sorted?

not really any data structure

- sort the array
- initialize another array to keep the merged part 
--- getting the end of the last item in new lst and comparing it with start of the 
--- current interval
--- everytime we merge, we increase the count once

thjis the wrong approach because it is the minimum interval to be removed
- not so much about the range overlap
e.g: [[1,100],[11,22],[1,11],[2,12]]
- [1,100]: need to remove 3
- [[1,11], [11,22]]: need to remove only 2 --> so the answer here is 2

does that mean we need to consider every combination?




'''

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        if len(intervals) ==  0 or not intervals:
            return 0
        
        intervals.sort()
       
        res = 0

        
        for i in range(len(intervals)):
            if i == 0:
                end = intervals[i][1] #save the end of first
                continue
            #[2,3] [2,4]
            elif intervals[i][0] >= end:
                end = intervals[i][1]
            else:
                #greater than prev
                res += 1
                end = min(intervals[i][1], end)
            

        return res
        
             


        