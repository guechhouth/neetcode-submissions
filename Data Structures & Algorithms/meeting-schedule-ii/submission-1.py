"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda i: i.start)
        min_heap = []

        for i in intervals:
            if min_heap and min_heap[0] <= i.start:
                heapq.heappop(min_heap) #pop and reuse the room
            heapq.heappush(min_heap, i.end) #push current meeting end time
        return len(min_heap)
       

            

        
        