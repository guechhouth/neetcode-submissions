# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lst = deque([root])
        res = []

        while lst:
            level = []
            length = len(lst)

            for i in range(length):
                node = lst.popleft()
                if node:
                    level.append(node.val)
                    lst.append(node.left)
                    lst.append(node.right)
            if level:
                res.append(level)
        return res

                    
        