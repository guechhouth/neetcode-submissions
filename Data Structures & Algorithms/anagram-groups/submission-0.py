from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #hashmap
    #["act": ["act", "cat"], "aht": ["hat"], ...]
        lst = []
        if len(strs) == 0:
            return lst
        
        
        dct = defaultdict(list)
        
        for val in strs:
            key = str(sorted(val))
            if key not in dct:
                dct[key].append(val)
            else:
                dct[key].append(val)
                
        for key, val in dct.items():
            lst.append(val)
        return lst

    

        
        