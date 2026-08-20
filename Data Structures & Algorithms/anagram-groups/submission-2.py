from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_map = defaultdict(list) # key=tuple of dict, val=list of words anagram
        
        for word in strs:
            w = defaultdict(int) # w can be in different orders, need to sort   
            sorted_word = sorted(word)
            for c in sorted_word:
                w[c] += 1
            # add to group_map
            group_map[tuple(w.items())].append(word)
          
        return list(group_map.values()) # .values give object

                

        