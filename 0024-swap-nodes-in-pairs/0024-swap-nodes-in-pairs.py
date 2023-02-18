# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(None, head)
        prev, curr1, curr2  = dummy, head, head.next
        while curr1 and curr2:
            prev.next, curr1.next, curr2.next = curr2, curr2.next, curr1
            prev = curr1
            curr1 = curr1.next
            if curr1:
                curr2 = curr1.next
            
        return dummy.next