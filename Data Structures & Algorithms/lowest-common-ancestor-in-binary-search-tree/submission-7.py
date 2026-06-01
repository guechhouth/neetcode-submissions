# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
1. need to know that both nodes are in the tree
2. if either node is the child of the other --> exist, return parent
3. if not and exist -> need to find the parent of both nodes

edge case:
1. one node, with p =q= that node then return that node
2. if p and q is null --> do they have common ancester?
'''
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr =  curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                #If one of p or q is less than curr.val and the other is greater 
                #(or one of them is equal to curr):
                #Then curr is the lowest common ancestor, 
                #because it’s the first node where the paths to p and q split 
                #(or stop if one is curr itself)
                return curr
        '''
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                #p.val > curr.val and q.val < curr.val
                #p.val < curr.val and q.val > curr.val
                return curr
            






















        
