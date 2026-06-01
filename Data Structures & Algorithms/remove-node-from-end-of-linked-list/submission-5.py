# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''understand
time and space: O(N), O(1)

'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #reverse the list
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        #traverse the list for the n counter
        c = 0
        dummy = ListNode(0)
        dummy.next = prev
        remove = dummy
        while remove.next:
            if c+1 ==n :
                remove.next = remove.next.next
                break
            remove = remove.next
            c +=1
        
        #now reverse back the list
        final = dummy.next
        tail = None
        while final:
            tmp = final.next
            final.next = tail
            tail = final
            final = tmp
        return tail


        
        
        