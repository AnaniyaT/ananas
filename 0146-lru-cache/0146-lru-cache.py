class ListNode:
    def __init__(self, key=0, val=0, nextt=None, prev=None):
        self.val = val
        self.next = nextt
        self.key = key
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = ListNode()
        self.tail = ListNode()
        self.dict = {}
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def remove(self, node):
        prev = node.prev
        nextt = node.next
        
        prev.next = nextt
        nextt.prev = prev
        
    def addHead(self, node):
        headNext = self.head.next
        
        self.head.next = node
        node.prev = self.head
        node.next = headNext
        headNext.prev = node
        
    def nextVictim(self):
        return self.tail.prev

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        
        node = self.dict[key]
        self.remove(node)
        self.addHead(node)
        
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key not in self.dict:
            newNode = ListNode(key, value)
            self.addHead(newNode)
            self.dict[key] = newNode
            
            if len(self.dict) > self.cap:
                victim = self.nextVictim()
                self.dict.pop(victim.key)
                self.remove(victim)
                
        else:
            node = self.dict[key]
            node.val = value
            self.remove(node)
            self.addHead(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)