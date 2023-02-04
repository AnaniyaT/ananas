# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        leftSide = ListNode()
        rightSide = ListNode()
        currLeft = leftSide
        currRight = rightSide
        while head:
            if head.val < x:
                currLeft.next = ListNode(head.val)
                currLeft = currLeft.next
            else:
                currRight.next = ListNode(head.val)
                currRight = currRight.next
                
            head = head.next
            
        currLeft.next = rightSide.next
        
        return leftSide.next