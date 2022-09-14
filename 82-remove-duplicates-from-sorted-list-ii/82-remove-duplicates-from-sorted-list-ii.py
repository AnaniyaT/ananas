# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        prev, curr, currval = dummy, head, None
        while curr and curr.next:
            if (currval != curr.val) and (curr.val != curr.next.val):
                prev.next = curr
                prev = curr
                curr = curr.next
            else:
                currval = curr.val
                curr = curr.next
        if curr and curr.val == currval:
            prev.next = None
        else:
            prev.next = curr
        return dummy.next
            
            
            