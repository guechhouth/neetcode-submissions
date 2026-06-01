# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
# 1->2 : 2 -> 1
# 1->2->3 : 3->1->2
n-1,1
n-2,2
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #slow and fast pointers
        s,f = head, head.next
        dummy = ListNode(0)
        tail = dummy

        while f and f.next:
            s = s.next
            f = f.next.next #1-2-3-4
        
        #f is at end
        #s is at the 'middle'
        
        #reverse the second half of the linkedlist
        curr = s.next
        prev = s.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        #replace s by prev: 6->5->4
    
    

        # 1->2->3->6->5->4

        second = prev
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

       
        

        

        
            
        