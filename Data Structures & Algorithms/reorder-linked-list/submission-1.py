# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #using slow and fast pointer to get the mid and end
        #1->2->3->4->5->6
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #slow and fast, reverse for from slow to fast
        #make sure to disconnect slow from first node
        curr = slow.next
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        slow.next = None

        second = prev
        first = head
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            head = head.next
            second.next = t1
            first = t1
            second = t2
    

    
        

        