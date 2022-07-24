# Definition for singly-linke d list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return None
        currnode = head
        prevnode = None
        while currnode.next != None:
            if currnode.val == val and prevnode == None:
                tempnode = currnode.next
                currnode = tempnode
                head = currnode
            elif currnode.val == val:
                prevnode.next = currnode.next
                currnode = prevnode.next
            else:
                prevnode = currnode
                currnode = currnode.next
        if currnode.val == val: 
            if prevnode != None: prevnode.next = None
            else:
                head = None
        return head
            
            
                