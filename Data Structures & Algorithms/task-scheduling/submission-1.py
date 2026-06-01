"""
inputs:
- tasks[i] = A-Z
- n: 

identical tasks must be seperated by at least n CPU cycles, to cooldown to CPU

min number of CPU cycles required

example:
X,X,Y,Y n = 2
X (1) -> Y (1) -> Idle (1) -> X (1) -> Y (1) = 5

A,A,A,B,C n = 3
A (1) -> B (1) -> C (1) -> Idle (1) -> A (1) -> Idle (1) -> Idle (1) -> Idle (1) -> A (1)
= 9
A - - - A - - - B C:  X

can we do a max-heap

what is there are a few cool down??
pq 

analysis
- map: O(n)
- while: O(n)
- heapify: O(k) -unique tasks = 26
- heappush/heappop: O(logk)
total: nlogk 
"""
import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # create a hashmap of key and value
        hmap = {}
        for i in tasks:
            hmap[i] = hmap.get(i, 0) + 1
        
        # max heap
        heap = [-cnt for cnt in hmap.values()]
        heapq.heapify(heap)

        # cooldown queue
        cooldown = deque()
        time = 0
        
        while heap or cooldown: # as long as heap is not empty
            time += 1
            # pop first one
            if heap:
                count = heapq.heappop(heap) + 1
                if count < 0:
                    cooldown.append((count, time + n))
           
            # if front of queue is ready push back to heap
            if cooldown and cooldown[0][1] == time:
                # add back
                heapq.heappush(heap, cooldown.popleft()[0])
        return time

        

        