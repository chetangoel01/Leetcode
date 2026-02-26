# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newlist = ListNode()
        copy = newlist

        if not list1 and not list2:
            return list1
        if not list2:
            return list1
        if not list1:
            return list2

        while list1 and list2:
            if list1.val < list2.val:
                newlist.next = list1
                newlist = newlist.next
                list1 = list1.next
            else:
                newlist.next = list2
                newlist = newlist.next
                list2 = list2.next
        
        while list1:
            newlist.next = list1
            newlist = newlist.next
            list1 = list1.next
        
        while list2:
            newlist.next = list2
            newlist = newlist.next
            list2 = list2.next

        return copy.next