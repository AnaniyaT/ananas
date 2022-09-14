# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            nextt = slow.next
            slow.next = prev
            prev = slow
            slow = nextt
        if fast:
            slow = slow.next
        while prev:
            if prev.val != slow.val:
                return False
            prev, slow = prev.next, slow.next
        return True