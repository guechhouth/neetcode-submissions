class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #hashmap for adjacency list, undirected graph
        if len(edges) != n-1:
            return False
        tree = {i: [] for i in range(n)}
        for (c,n) in edges:
            tree[c].append(n)
            tree[n].append(c)

        
        #visit set to detect circle
        visit = set()
        def dfs(node,par):
            #has cycle
            if node in visit:
                return False
            visit.add(node)
            for c in tree[node]:
                if c == par:
                    continue
                if not dfs(c,node):
                    return False
            return True


    
        #dfs for circle detection
        if dfs(0,-1):
            return True
        else:
            return False

        #check that the len of set ==n
        if n == len(visit):
            return True
        else:
            return False
        



        