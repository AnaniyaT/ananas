class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None for _ in range(26)]
        self.value = 0
        
class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for c in key:
            ind = ord(c.lower()) - ord("a")
            if not cur.children[ind]:
                cur.children[ind] = TrieNode()
            cur = cur.children[ind]
                
        cur.isEnd = True
        cur.value = val

    def sum(self, prefix: str) -> int:
        cur = self.root
        
        for c in prefix:
            ind = ord(c.lower()) - ord("a")
            if not cur.children[ind]:
                return 0
            cur = cur.children[ind]
            
        summ = 0
        def trav(node):
            nonlocal summ
            if not node:
                return
            
            if node.isEnd:
                summ += node.value
                
            for ind in range(26):
                trav(node.children[ind])
                
        trav(cur)
        return summ
        
        
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)