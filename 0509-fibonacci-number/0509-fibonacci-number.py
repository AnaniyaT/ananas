class Solution:
    def __init__(self):
        self.fibList = [0, 1]
        
    def fib(self, n: int) -> int:
        if n < len(self.fibList):
            return self.fibList[n]
        
        before = self.fib(n-2)
        after = self.fib(n-1)
        
        self.fibList.append(before + after)
        
        return self.fibList[n]