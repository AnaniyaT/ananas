class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0]*k
        self.l = 0
        self.r = 0
        self.size = k

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.queue[self.r%self.size] = value
            self.r += 1
        else:
            return False
        
        return True
            

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.l += 1
        else:
            return False
        
        return True

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[(self.l)%self.size]
        else:
            return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[(self.r-1)%self.size]
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.l == self.r

    def isFull(self) -> bool:
        return (self.r - self.l) == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()