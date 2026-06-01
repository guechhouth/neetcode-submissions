
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]
        dct = {}

        for i in strs:
            alphaMap = {i: 0 for i in range(26)}

            for j in i:
                alphaMap[ord(j)- ord('a')] += 1
                print(alphaMap)
            
            if tuple(alphaMap.values()) not in dct:
                dct[tuple(alphaMap.values())] = [i]
            else:
                dct[tuple(alphaMap.values())].append(i)
        print(dct)
        
        lst = []
        for v in dct.values():
            lst.append(v)
        return lst 
           

        