# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        lst = []
        
        if not root:
            return lst

        q = deque([root])
        
        while q:
            sublst = []
            numItem = len(q)

            while numItem > 0:
                item = q.popleft()
                numItem -= 1

                if item:
                    sublst.append(item.val)
                    q.append(item.left)
                    q.append(item.right)
            lst.append(sublst) if sublst else None
               
        return lst
        '''
        lst = []

        if not root:
            return lst

        curr = deque([root])

        while curr:
            sublst = []
        
            for i in range(len(curr)):
                node = curr.popleft()
                if node:
                    sublst.append(node.val)
                    curr.append(node.left)
                    curr.append(node.right)
            if sublst:
                lst.append(sublst)


        return lst



















            

    
        