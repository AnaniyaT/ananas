# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        prev = None
        maxx = 0
        while fast and fast.next:
            fast = fast.next.next
            nextt = slow.next
            slow.next = prev
            prev = slow
            slow = nextt
        while prev:
            maxx = max(maxx, prev.val + slow.val)
            prev, slow = prev.next, slow.next
        return maxx