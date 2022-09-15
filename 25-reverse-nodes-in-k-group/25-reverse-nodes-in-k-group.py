# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        l = r = head
        n = 1
        while n<k:
            r = r.next
            if not r:
                return l
            n += 1
        prev = self.reverseKGroup(r.next, k)
        for i in range(k):
            nextt = l.next
            l.next = prev
            prev = l
            l = nextt
        return prev
        