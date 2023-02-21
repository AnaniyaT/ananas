# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        tail = head
        size = 1
        while tail.next:
            tail = tail.next
            size += 1
        
        k %= size
        curr = head
        for _ in range(size-k-1):
            curr = curr.next
            
        tail.next = head
        head = curr.next
        curr.next = None
        
        return head
        