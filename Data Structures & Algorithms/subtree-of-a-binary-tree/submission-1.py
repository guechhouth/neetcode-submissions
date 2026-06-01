# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
1. find the whether the root of subroot is in the root
-> DFS on left and right
-> if we could not find then return False immediately
2. if it is, from here, we start comparing the children left and right
    -> a second function to check for this
3. return the value

edge case:
1. if both trees are null, are they the same? yes
2. if subTree empty -> is it a subtree of non-empty tree? yes
'''
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        #if s is empty and t is not
        if not root: return False

        if self.sameTree(root,subRoot):
            return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def sameTree(self, s, t):
        if not s and not t: #same tree
            return True
        
        if s and t and s.val == t.val:
            return self.sameTree(s.left,t.left) and  self.sameTree(s.right,t.right)

        return False
        