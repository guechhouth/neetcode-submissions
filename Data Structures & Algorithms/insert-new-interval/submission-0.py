class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:   
        res = []

        #add interval before overlap
        k = 0
        while k < len(intervals) and intervals[k][1] < newInterval[0]:
            res.append(intervals[k])
            k+=1

        #add overlap interval
        while k < len(intervals) and intervals[k][0] <= newInterval[1]:
            newInterval[0] = min(intervals[k][0], newInterval[0])
            newInterval[1] = max(intervals[k][1], newInterval[1])
            k+= 1
        res.append([newInterval[0], newInterval[1]])

        #add interval after overlap
        while k < len(intervals):
            res.append(intervals[k])
            k+=1 
        return res



        
        