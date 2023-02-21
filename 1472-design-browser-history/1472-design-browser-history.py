class DoubleNode:
    def __init__(self, page="", next=None, prev=None):
        self.page = page
        self.next = next
        self.prev = prev
    
class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = DoubleNode(homepage)

    def visit(self, url: str) -> None:
        self.current.next = DoubleNode(url, prev=self.current)
        self.current = self.current.next
    
    def back(self, steps: int) -> str:
        count = 0
        while self.current.prev and count < steps:
            self.current = self.current.prev
            count += 1
            
        return self.current.page

    def forward(self, steps: int) -> str:
        count = 0
        while self.current.next and count < steps:
            self.current = self.current.next
            count += 1
            
        return self.current.page


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)