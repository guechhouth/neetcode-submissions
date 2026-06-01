class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #construct map for the graph
        graph = {i: [] for i in range(numCourses)}
        for (c,p) in prerequisites:
            graph[c].append(p)

                
        #use set to track each path
        visit = set()
        #when there is cycle --> some courses cant be completed before completing the other
        #when ever that is reached return false
        #if none are reached return true
            #do dfs
        def dfs(c):
            if c in visit:
                #cycle
                return False
            visit.add(c)
            for pre in graph[c]:
                if not dfs(pre):
                    return False
            visit.remove(c)
            graph[c] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


        
        


        