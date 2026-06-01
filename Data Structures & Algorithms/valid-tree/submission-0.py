'''
clarifying question:
- will there be duplicate edges? 
- does [0,1] = [1,0] = yes since it is undirected

understand: given n nodes: 0-(n-1)
undirected edges
--> check if the edges make up a valid tree

what is a valid tree? 
- if there is a cycle
- if there is a disconnection
- if n node than has n-1 edges

Approach:
- use dfs
- use hashmap to store the start and end nodes. 
- use visited set to check if the node alr has been visited if it 
is , then it is a cycle
- how to make sure that there is no disconnection?
- after visited, we should pop and empty it

{
    0 : [1]
    1 : [2,3,4]
    2 : [3]

}

'''

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #verify the edge
        if len(edges) != n-1:
            return False
        #add in hashmap
        edgeMap = {i:[] for i in range(n)}

        for pre,nex in edges:
            #[0,1] adding node and direction
            edgeMap[pre].append(nex)
            edgeMap[nex].append(pre)
        '''
        adjacency list
        {
            0 : [1]
            1 : [0,2,3,4]
            2 : [1,3]
            3 : [2,1]
            4 : [1]
        }
        '''
        
        #visited set to track circle
        visited = set()

        def dfs(prev, parent):
            if prev in visited:
                return False
            visited.add(prev)
            #visit neighbor of the node

            for nex in edgeMap[prev]:
                if nex == parent:
                    continue
                #e.g: [1]
                if not dfs(nex, prev):
                    return False
            return True
        if not dfs(0,-1):
            return False
        if len(visited) == n:
            return True
                
            
        