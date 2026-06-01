# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
preorder: first element is root
inorder: from pre-order, we can find root
<-root: left subtree
root->: right subtree

edge:
is there any duplicate?

facts:
- first value in pre-order is ROOT
    - first value after that is always gonna be the ROOT of left subtree
    right after the left subtree done-> the next val would be the root of right subtree
- preorder[1:] --> which go to left and right subtree
    - inorder array: at root
    - left of root: all val in left subtree
    - right of root: all val in the right sbutree

'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        if not preorder and not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
        '''
        if not preorder and not inorder:
            return None
        root = TreeNode(preorder[0])
        m = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:m+1], inorder[:m])
        root.right = self.buildTree(preorder[m+1:], inorder[m+1:])
        return root























        