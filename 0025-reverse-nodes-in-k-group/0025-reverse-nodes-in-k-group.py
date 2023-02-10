# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        newCurr = dummy
        curr = head
        first = None
        
        for i in range(k):
            if not curr:
                return head
            temp = ListNode(curr.val, dummy.next)
            
            first = temp if not i else first
            dummy.next = temp
            curr = curr.next
            
        first.next = self.reverseKGroup(curr, k)
        
        return dummy.next
        