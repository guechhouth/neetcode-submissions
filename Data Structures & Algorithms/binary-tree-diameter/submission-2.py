# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter = start from root depth to right + depth_left
        maxDiameter = [0]
        def dfs(node, maxDiameter):
            if not node:
                return -1 # for edge
            else:
                # height of current node
                left = dfs(node.left, maxDiameter)
                right = dfs(node.right, maxDiameter)
                curr = left + right + 2
                maxDiameter[0] = max(maxDiameter[0], curr)
                return 1 + max(dfs(node.left, maxDiameter), dfs(node.right, maxDiameter) )
    
        dfs(root, maxDiameter)
        return maxDiameter[0] 
        