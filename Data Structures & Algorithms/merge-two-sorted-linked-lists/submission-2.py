# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curOne = list1
        curTwo = list2
        newList = ListNode(0)
        dummy = newList
        while curOne and curTwo:
            if curOne.val <= curTwo.val:
                dummy.next = curOne
                curOne = curOne.next
            else:
                dummy.next = curTwo
                curTwo = curTwo.next
            dummy = dummy.next
            
           
        if curOne:
            dummy.next = curOne
        else:
            dummy.next = curTwo
        return newList.next


        