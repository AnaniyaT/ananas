class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None for _ in range(26)]
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            ind = ord(c.lower()) - ord("a")
            if not cur.children[ind]:
                cur.children[ind] = TrieNode()
            cur = cur.children[ind]
                
        cur.isEnd = True
    
    def getLongest(self) -> str:
        word = ''
        cur = []
        
        def trav(node):
            nonlocal word
            if len(cur) > len(word):
                word = "".join(cur)
                
            for ind in range(26):
                child = node.children[ind]
                if child and child.isEnd:
                    lett = chr(ord("a") + ind)
                    cur.append(lett)
                    trav(child)
                    cur.pop()
        
        trav(self.root)
        return word
            
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        return trie.getLongest()
            
        