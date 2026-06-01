"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

'''
EMPHASIS ON THE CLONE: CLONE MEANS SAME STRUCTURE BUT THE NODES ARE NEW NODES
connected, undirected graph = no arrows
index = node value
at each index (node value) = lst of the adjacent nodes

given a node, return a deep copy of the graph
node.val = access the val = index of the graph we want to return
node.neighbors = list of all neighbors

1. use dictionary:
key = node's index
value = neightbors list

2. for each iteration of the node -> only add to the dictionary when the key
is not in it

3. how to know when to end? how to keep feeding new node? 
--> have a visited set where we store all the unque neightbor 
if there is additional neighbor that is exactly equal to what is in the set, we know that we have
finished?

'''


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloneSet = {}


        def clone(node):
            if node in cloneSet:
                return cloneSet[node]

            copy = Node(node.val)
            cloneSet[node] = copy
            
            for i in node.neighbors:
                copy.neighbors.append(clone(i))

            return copy

        return clone(node) if node else None

        

        