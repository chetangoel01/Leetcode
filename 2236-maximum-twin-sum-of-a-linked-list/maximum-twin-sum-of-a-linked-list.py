# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverseList(head):
            prev = None
            curr = head
            while curr:
                nextPointer = curr.next
                curr.next = prev
                prev = curr
                curr = nextPointer
            return prev

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        midPoint = reverseList(slow)
        maxTwin = -1
        slow = head
        fast = midPoint
        while fast:
            maxTwin = max(maxTwin, slow.val + fast.val)
            slow = slow.next
            fast = fast.next
        
        return maxTwin