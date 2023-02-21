# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddDummy = ListNode(next=head)
        evenDummy = ListNode()
        if head:
            evenDummy.next = head.next
        else:
            return head
            
        currOdd = oddDummy.next
        currEven = evenDummy.next
        
        while currEven and currEven.next:
            currOdd.next = currEven.next
            currEven.next = currEven.next.next
            
            currOdd = currOdd.next
            currEven = currEven.next
            
        currOdd.next = evenDummy.next
        
        return oddDummy.next
        