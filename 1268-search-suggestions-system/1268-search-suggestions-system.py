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
    
    def __getWords(self, c: TrieNode, pre: str = "") -> list[str]:
        words = []
        letters = []
        
        def rec(c: TrieNode):
            if not c or len(words) >= 3:
                return
            
            if c.isEnd:
                words.append(pre + "".join(letters))
            
            for ind in range(26):
                if c.children[ind]:
                    letters.append(chr(ord("a") + ind))
                    rec(c.children[ind])
                    letters.pop()
        
        rec(c)
        return words
    
    def getWordsByPrefix(self, prefix: str) -> list[str]:
        cur = self.root
        for c in prefix:
            ind = ord(c.lower()) - ord("a")
            if not cur.children[ind]:
                return []
            
            cur = cur.children[ind]
            
        return self.__getWords(cur, pre=prefix)
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)
            
        ans = []
        for ind in range(1, len(searchWord) + 1):
            ans.append(trie.getWordsByPrefix(searchWord[:ind]))
            
        return ans
        