class MyQueue(object):

    def __init__(self):
        self.stk1, self.stk2 = [], []

    def push(self, x):
        while self.stk1:
            self.stk2.append(self.stk1.pop())
        self.stk1.append(x)
        while self.stk2:
            self.stk1.append(self.stk2.pop())
            
    def pop(self):
        return self.stk1.pop()
    
    def peek(self):
        if self.stk1:
            return self.stk1[-1]
        
    def empty(self):
        return not self.stk1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()