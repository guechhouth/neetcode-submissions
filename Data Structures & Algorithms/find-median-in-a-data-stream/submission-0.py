'''
1. Brute force:
- data structure: array
- keep adding at the back
- then sort
- to find median -> find len and divide by 2 if it is int --> access that eleemnt if not take average
between item before and after 
- return the median
Time complexity:
- O(1) adding at the back and O(nlogn) for sorting
- find median: O(N) for traversing, O(1) for accessing value 

2. prirotity queue
ascending order: small -> big
add -> need to find right space to maintain the order
PQ: min-heap -> percolate up to find the right space

- adding would take O(logn) = height, find median O(N)

- insert in minheap:  
    -> add new node at leaf most leave available
    -> percolate up if needed, continuosly swapping with parent if needed
    -> stop when its not small than parent
- finding median
    -> pq -> popleft: small -> big


3. clarifying question: 
- do i have to implement prioty queue from scratch ir can i use the existing function?
'''
class MedianFinder:

    def __init__(self):
        self.small = [] #max heap - [0] = max
        self.large = [] #min heap -[0] = min
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        #check that all item in small is <= large. i.e max in small is <= min in large
        if self.small and self.large and (-1 * self.small[0] > self.large[0]):
            #pop max from small and add to large
            val = -1 * heapq.heappop(self.small) #by default, python heap is min heap
            heapq.heappush(self.large, val)
        
        #check that the length is about the same
        if len(self.small) > len(self.large) + 1:
            #pop max from small and add to large
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val =  heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)


    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        
        return (-1 * self.small[0] + self.large[0])/2


        
        
        