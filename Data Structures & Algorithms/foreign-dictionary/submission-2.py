'''
1. if we do some kind of dfs on the word how?
["hrn","hrf","er","enn","rfnn"]

for letter in word hrn and letter in hrf
- if they are the same --> skip
- if they are not the same --> we want to find their order
---how? try adjacency list : like pre-req question so we have 
--- n < f



- dictionary
dict = {
    "n": "f",
    "h": "e",
    "r": "n",
    "e": "r"
}

2. for each key in the map
- we run dfs on the key  --> if there is a cycle --> fail
- keep track of the length of the word -> we len == number of unique
character --> then we reach our word



'''

from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #edge cases
        if len(words) == 1:
            return words[0]
        if len(words) == 0 or not words:
            return ""

        #step 1: build adjacency list
        adj = defaultdict(list)
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            k = 0
            #after the length --> we can't determined the order anymore
            while k < min(len(w1), len(w2)):
                if len(w1) > len(w2) and w1.startswith(w2):
                    return ""
                #can't use the logical comparison here cuz it will use ascii
                if w1[k] != w2[k]:
                    adj[w1[k]].append(w2[k])
                    break
                k += 1
        unque = set()
        for w in words:
            for c in w:
                unque.add(c)
        #add the rest of the character
        for c in unque:
            if c not in adj:
                adj[c] = []

        print(adj)

        #step 2: run dfs for each key of the adj list
        
        #2.1 dfs function
        self.cycle = False
        self.word = ""
        visited = set()
        visiting = set()
        def dfs(c):
            #edge case
            if c in visiting:
                self.cycle = True
                return
            if c in visited:
                return
            visiting.add(c)
            #recursive case
            for nei in adj[c]:
                dfs(nei)
            visiting.remove(c)
            visited.add(c)
            self.word += c

        #2.2 go through each key in dictionary
        for k in list(adj.keys()):
            #run dfs on k
            dfs(k)
        #compare the word length and cycle flag
        if len(self.word) == len(unque) and not self.cycle:
            return self.word[::-1]
        #can't find the correct order
        return ""
