class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = [0]*k
        self.size = k
        self.l = 0
        self.r = 0
        
    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.l -= 1
            self.queue[self.l%self.size] = value
        else:
            return False
        
        return True

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.queue[self.r%self.size] = value
            self.r += 1
        else:
            return False
        
        return True

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.l += 1
        else:
            return False
        
        return True

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.r -= 1
        else:
            return False
        
        return True

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.queue[self.l%self.size]
        else:
            return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.queue[(self.r-1)%self.size]
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.r == self.l

    def isFull(self) -> bool:
        return self.r - self.l == self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()