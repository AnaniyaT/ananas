# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack, arr = [], []
        curr, indx = head, 0
        while curr:
            while stack:
                if stack[-1][0] < curr.val:
                    pair = stack.pop()
                    arr[pair[1]] = curr.val
                else: 
                    break
            arr.append(0)
            stack.append([curr.val,indx])
            indx += 1
            curr = curr.next
        return arr
                    
                    