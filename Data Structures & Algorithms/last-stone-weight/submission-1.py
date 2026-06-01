import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # create a max_heap
        max_heap = [-x for x in stones]
        # max heapify 
        heapq.heapify(max_heap)
        print(f"stone: {max_heap}")

        while len(max_heap) > 1:
            # pop the two most heaviest 
            h1 = -1 * heapq.heappop(max_heap)
            h2 = -1 * heapq.heappop(max_heap)
            if (h1) > (h2):
                new_weight = h1 - h2
                heapq.heappush(max_heap, -1 * new_weight)
                heapq.heapify(max_heap)
        return 0 if (len(max_heap) == 0) else -1 * max_heap[0]      