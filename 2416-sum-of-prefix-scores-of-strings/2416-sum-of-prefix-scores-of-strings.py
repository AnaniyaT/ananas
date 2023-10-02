class TrieNode:
    def __init__(self):
        self.count = 0
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
            cur.count += 1
    
    def getScore(self, word: str) -> int:
        score = 0
        cur = self.root
        for c in word:
            ind = ord(c.lower()) - ord("a")
            if not cur.children[ind]:
                return score
            
            cur = cur.children[ind]
            score += cur.count
            
        return score
    
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
            
        return [trie.getScore(word) for word in words]