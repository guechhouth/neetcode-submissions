# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
need to search for the whole thing?
- maybe in order traversal and populate everything so far in an array
- continuously check if the array's length is k or not
- if it is, return the k index val right away
- if not, continue the operation
- if length is < k at the end then, return None
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        if not root:
            return None
        lst = []

        def inOrder(root, k, lst):
            if not root:
                return
            
            inOrder(root.left, k,lst)
            lst.append(root.val)
            inOrder(root.right,k,lst)

            return lst
        
        inOrder(root,k,lst)
        if k <= len(lst):
            return lst[k-1]
        else:
            return None

        #O(N) time: in-order traversal = O(N), accessing element in array O(1)
        #O(N) space: new lst O(n), and call stack O(h)
        '''
        if not root:
            return None
        lst = []
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            lst.append(node.val)
            inOrder(node.right)
        inOrder(root)
        if len(lst) >= k:
            return lst[k-1]
        else:
            return None






















        