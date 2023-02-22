# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = ListNode(next=list1)
        curr2 = list2
        
        head = curr1
        
        while curr2:
            while curr1.next and curr1.next.val <= curr2.val:
                curr1 = curr1.next
            
            nextt = curr2.next 
            curr2.next = curr1.next
            curr1.next = curr2
            curr2 = nextt
            
        return head.next
        