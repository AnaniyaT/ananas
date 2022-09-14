# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        slow.next = prev = None
        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        insertafter = head
        while prev:
            nextt = prev.next
            prev.next = insertafter.next
            insertafter.next = prev
            insertafter = prev.next
            prev = nextt
            