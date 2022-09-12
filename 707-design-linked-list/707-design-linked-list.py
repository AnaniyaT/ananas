class Node:
    def __init__(self,val = None, next = None):
        self.val = val
        self.next = next
        
class MyLinkedList:
    
    def __init__(self):
        self.size = 0
        self.head = None

    def get(self, index: int) -> int:
        if not index < self.size:
            return -1
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val)
        else:
            self.head = Node(val, self.head)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index <= self.size:
            curr = self.head
            for i in range(index-1):
                curr = curr.next
            curr.next = Node(val, curr.next)
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < self.size and index >= 0:
            if index == 0:
                self.head = self.head.next
            else:
                curr = self.head
                for i in range(index-1):
                    curr = curr.next
                curr.next = curr.next.next
            self.size -= 1
                
                


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)