# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #do dfs with inorder traversa
        #in order traversal: left, self, right
        self.result = None
        self.count = 0
        
        def dfs(node):
            #found the kth smallest number
            if not node or self.result is not None:
                return
            #call dfs on the left
            dfs(node.left)
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            
            #call dfs on the right
            dfs(node.right)

        dfs(root)
        return self.result


        