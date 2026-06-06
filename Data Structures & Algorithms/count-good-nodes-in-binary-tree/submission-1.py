# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
do dfs
track greatest value on the path 
compared greatest to the current if current is bigger than is valid
"""

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # global var to count number of good nodes
        def dfs(node, maxVal):
            if not node:
                return 0 
            is_good = 1 if node.val >= maxVal else 0
            # this node is greater
            maxVal = max(maxVal, node.val)
            left_good = dfs(node.left, maxVal)
            right_good = dfs(node.right, maxVal)
            return is_good + left_good + right_good
        return dfs(root, root.val)

        