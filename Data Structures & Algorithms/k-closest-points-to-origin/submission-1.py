import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # check the length of the points
        if len(points) < k:
            return []
        # construct a min heap with ([x,y], euclidean_dist)
        min_heap = []
        for i in points:
            x = i[0]
            y = i[1]
            dist = (x**2 + y**2) # don't even need sqrt
            min_heap.append((dist, i))
        
        # heapify by first element dist
        heapq.heapify(min_heap) 
        # k closest to orgiin
        res = []
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])
        
        return res
        

