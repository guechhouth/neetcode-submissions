"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
#brute force just compare every pair: O(n^2)

#sorting custom object
# need to specify key and the sort by criteria

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        if not intervals:
            return True
        #sort
        intervals.sort(key=lambda i: i.start)
        prev = intervals[0].end
        

        for i in range(1, len(intervals)):
            if intervals[i].start < prev:
                return False
            prev = max(intervals[i].end, prev)
        return True

