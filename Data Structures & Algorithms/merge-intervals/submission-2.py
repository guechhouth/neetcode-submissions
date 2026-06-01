class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        #l1, r1 and l2, r2
        
        #sort interval
        intervals.sort()
        res = []
        res.append(intervals[0])

        for s,e in intervals:
            l2 = res[-1][1]

            if s <= l2:
                res[-1][1] = max(l2, e)
            else:
                res.append([s,e])
        return res
            
                        

        