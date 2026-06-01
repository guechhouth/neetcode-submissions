class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # hashmap for s1
        s1Map = {}
        for i in s1:
            if i not in s1Map:
                s1Map[i] = 1
            else:
                s1Map[i] += 1
        # hasmap for s2
        s2Map = {}
        total_char = 0
        for i in range(0, len(s2)): # shift forward by one each time
            c = s2[i]
            if c not in s2Map:
                s2Map[c] = 1
            else:
                s2Map[c] += 1 

            # shrink from left if s >= len(s1)
            if i >= len(s1):
                l = s2[i - len(s1)]
                s2Map[l] -= 1
                if s2Map[l] == 0:
                    del s2Map[l]
            if i >= len(s1) - 1:
                if s1Map == s2Map:
                    return True
        return False
            