# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #for loop through the array two step at the time
        #what if the array length is odd?
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            result = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None

                result.append(self.mergeLst(l1,l2))

            lists = result
        return lists[0] 

            #pick two at the time and continue merging it
        
    #helper function to merge two linkedlist
    def mergeLst(self, one, two):
        new = ListNode()
        dummy = new
        while one and two:
            if one.val <= two.val:
                dummy.next = one
                one = one.next
            else:
                dummy.next = two
                two = two.next
            dummy = dummy.next
        if one:
            dummy.next = one
        else:
            dummy.next = two
        return new.next
                    


        