class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        
class MyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        node = self.head.next
        for _ in range(index):
            node = node.next
            
        return node.val

    def addAtHead(self, val: int) -> None:
        self.head.next = Node(val, self.head.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 
        curr = self.head
        for _ in range(index):
            curr = curr.next
        temp = curr.next
        node = Node(val, temp)
        curr.next = node
        self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        curr = self.head
        for _ in range(index):
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