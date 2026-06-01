'''
return the number of graphs that are connected, leave ones that are not

{
    0 : [1,2],
    1 : [0],
    2 : [0]
}

if n == 1: return 1
is the graph valid --> yes

#this check is vlaid for tree not general graph, this question is general graph
if len(edges) != n-1:
    return None

'''


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        #edge case
        if n == 0:
            return count
        #create map
        graph = {i:[] for i in range(n)}
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        '''
        {
            0 : [1],
            1 : [0,2],
            2 : [1,3],
            3 : [2],
            4 : [5],
            5 : [4],
        }

        '''
        visit = set()
        def dfs(node, parent):
            #backtracking base case
            if node in visit:
                return
            visit.add(node)

            #visit neighbor
            for nei in graph[node]:
                if nei == parent:
                    continue
                dfs(nei, node)
            
            #base case: done with a tree
            return
        #loop through the graph
        for i in range(n):
            if i not in visit:
                dfs(i,-1) #return true
                count += 1
        return count
            

        
        