class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in nums:
            map[i] = 1 + map.get(i, 0)
        
        res = []
        maxV = float('-inf')
      
        seen = set()
        while k > 0:
            for n,v in map.items():
                if v >= maxV and n not in seen:
                    maxV = v
                    maxN = n
            if maxN not in seen:
                res.append(maxN)
                k -= 1
                seen.add(maxN)
                maxV =float('-inf')
        return res
            
        