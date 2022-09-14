# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self,head1, head2):
        curr = dummy = ListNode()
        curr1, curr2 = head1, head2
        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next
        while curr1:
            curr.next = curr1
            curr1 = curr1.next
            curr = curr.next
        while curr2:
            curr.next = curr2
            curr2 = curr2.next
            curr = curr.next
        return dummy.next
            
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        fast = head
        slow = ListNode(next = head)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None
        
        return self.merge(self.sortList(head), self.sortList(right))