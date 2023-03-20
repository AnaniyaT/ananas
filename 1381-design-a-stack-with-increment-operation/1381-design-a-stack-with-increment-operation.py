class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) >= self.maxSize:
            return
        
        self.stack.append([0, x])

    def pop(self) -> int:
        if not self.stack:
            return -1
    
        inc, top = self.stack.pop()
        
        if self.stack and inc:
            self.stack[-1][0] += inc
        
        return inc + top
        
        
    def increment(self, k: int, val: int) -> None:
        if not self.stack:
            return
        
        ind = min(k - 1, len(self.stack) - 1)
        self.stack[ind][0] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)