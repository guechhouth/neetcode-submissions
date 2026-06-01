# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        prev = None
        for i in range(n):
            fast = fast.next
        while fast:
            prev = slow
            fast = fast.next
            slow = slow.next
        #now slow is at exact pos 
        #we need the reset the ref of the one before = prev
        if prev:
            prev.next = slow.next
        else:
            #there is nothing
            head = head.next
        return head
        