# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newlist = ListNode(0)
        curr = newlist
        point = curr
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                point.next = list1
                point = point.next
                list1 = list1.next
            else: 
                point.next = list2
                point = point.next
                list2 = list2.next
        if list1 is None:
            point.next = list2
        else:
            point.next = list1
            
        return curr.next
            

        