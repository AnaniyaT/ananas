class Solution:
    cachee = [0,1]
    def fib(self, n: int) -> int:
        if n < len(self.cachee):
            return self.cachee[n]
        self.cachee.append(self.fib(n-1)+self.fib(n-2))
        return (self.cachee[n])
        
        