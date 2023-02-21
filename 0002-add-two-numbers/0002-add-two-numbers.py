# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        keri = 0
        while l1 and l2:
            summ = l1.val + l2.val + keri
            curr.next = ListNode(summ%10)
            if summ > 9:
                keri = summ//10
            else:
                keri = 0
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            summ = l1.val + keri
            curr.next = ListNode(summ%10)
            if summ > 9:
                keri = summ//10
            else:
                keri = 0
            curr = curr.next
            l1 = l1.next
        while l2:
            summ = l2.val + keri
            curr.next = ListNode(summ%10)
            if summ > 9:
                keri = summ//10
            else:
                keri = 0
            curr = curr.next
            l2 = l2.next
        if keri:
            curr.next = ListNode(keri)
            
        return head.next