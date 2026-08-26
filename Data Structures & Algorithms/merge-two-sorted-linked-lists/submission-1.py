# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        dummy = ListNode()
        tail = dummy

        if list1.val < list2.val:
            tail.next = list1
            tail = tail.next
            tail.next = self.mergeTwoLists(list1.next, list2)
        
        else:
            tail.next = list2
            tail = tail.next
            tail.next = self.mergeTwoLists(list1, list2.next)
            
        return dummy.next
    
        