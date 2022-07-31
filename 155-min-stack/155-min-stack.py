class MinStack:

    def __init__(self):
        self.myStack = []
    def push(self, val: int) -> None:
        if len(self.myStack)==0:
            self.myStack += [[val,val]]
        else:
            if self.myStack[-1][1] < val:
                self.myStack += [[val,self.myStack[-1][1]]]
            else:
                self.myStack += [[val,val]]
    def pop(self) -> None:
        if len(self.myStack)==0:
            return
        del self.myStack[-1]
    def top(self) -> int:
        if len(self.myStack)==0:
            return
        return self.myStack[-1][0]
    def getMin(self) -> int:
        if len(self.myStack)==0:
            return
        return self.myStack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()