class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #use hashmap for couting the number of ccurence of each num in the list
        dct ={}
        lst = []
        count = 0
        for num in nums:
            if num not in dct:
                dct[num] = 1
            else:
                dct[num] += 1
        
        while count < k:
            maximum = -1
            keyVal = 0
            for key, val in dct.items():
                if val > maximum:
                    maximum = val
                    keyVal = key
            lst.append(keyVal) 
            del dct[keyVal] 
            count += 1
        return lst
            
            



        