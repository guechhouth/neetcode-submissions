# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#print from the back 
# a->b->c->d
#return: d->c->b->a

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        prev, curr = None, head

        #going through the list until the end
        while curr:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt
 
        return prev
        '''
        prev, curr = None, head

        while curr:
            nxt = curr.next #nxt = 1
            curr.next = prev
            prev = curr #prev = 0
            curr = nxt
        
        return prev




            


        

        
        