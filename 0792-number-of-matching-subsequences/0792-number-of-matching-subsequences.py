class TrieNode:
    def __init__(self):
        self.isEnd = 0
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
                
        cur.isEnd += 1

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        n = len(s)
        occ = [[] for _ in range(n)]
        cur = [-1] * 26

        for ind in range(n-1, -1, -1):
            occ[ind] = cur[:]
            lett = ord(s[ind]) - ord('a')
            cur[lett] = ind
            
        occ.append(cur)
        
        # for row in occ:
        #     print(row)
            
        trie = Trie()
        for word in words:
            trie.insert(word)
            
        subsequences = 0
        def trav(node, ind):
            nonlocal subsequences
            
            subsequences += node.isEnd
            
            for lett in range(26):
                if node.children[lett] and occ[ind][lett] != -1:
                    trav(node.children[lett], occ[ind][lett])
        
        trav(trie.root, -1)
        
        return subsequences
        
        