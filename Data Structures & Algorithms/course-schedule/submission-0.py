'''
clarifying question:
- is there max of numCourses? 1 <= x <=1000?
- is there any duplicate? no
- what happen if a class does not need prerequisite? does [1,1] count?
- [2,1], [2,7]: is this possible? like u can take same class, they are or requisites?

return true if it is possible to finish all courses
-> at least two courses are prerequisite of each other, can't take any

1. option 1
[1,0]: ok
[2,1]: ok
[3,0]: ok
[4,2]: ok
[5,1]: ok
[6,7]: not ok
[2,7]: is this possible? if this is possible then we have to check if 2 alr in the map
if it is then, we don't need to take 7 --> ok! if not 'not ok!'

{
    0: 1,3
    1: 2,5
    2: 4
    7
}

--> this needs traversal of hashmap, every single time? so O(n^2) time complexity

2. option 2
we could use a graph like hashmap
6
|
0--1--2
|  |  |
3  5  4 

this way when we go through, we only need to check each node at msot once
and then each edge once as well

- what data structure should i use?
-hashmap
-set = visit set
if a loop is detected that means we will not be able to complete the courses




'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crsReq = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            crsReq[crs].append(pre)
        
        #now that we got the map, we need go through the map
        visited = set()

        def dfs(crs):
            if crs in visited:
                #cycle detected
                return False
            if crsReq[crs]  == []:
                return True
            
            visited.add(crs)
            for pre in crsReq[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            crsReq[crs] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


            

        