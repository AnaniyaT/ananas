# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        for _ in range(left-1):
            curr = curr.next
            
        start = curr.next
        curr1 = start
        prev = None
        
        for _ in range(right-left+1):
            nextt = curr1.next
            curr1.next = prev
            prev = curr1
            curr1 = nextt
        
        curr.next = prev
        start.next = nextt
        
        return dummy.next
        