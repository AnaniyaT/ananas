# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        currl1, currl2 = list1, list2
        while currl1 and currl2:
            if currl1.val < currl2.val:
                curr.next = ListNode(currl1.val)
                curr = curr.next
                currl1 = currl1.next
            else:
                curr.next = ListNode(currl2.val)
                curr = curr.next
                currl2 = currl2.next
        while currl1:
            curr.next = ListNode(currl1.val)
            currl1 = currl1.next
            curr = curr.next
        while currl2:
            curr.next = ListNode(currl2.val)
            currl2 = currl2.next
            curr = curr.next
        return head.next
        