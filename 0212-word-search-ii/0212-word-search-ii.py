class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        n, m = len(board), len(board[0])
        cur, visited = [], [[0 for _ in range(m)] for _ in range(n)]
        
        def insert(word: str) -> None:
            cur = root
            for c in word:
                ind = ord(c.lower()) - ord("a")
                if not cur.children[ind]:
                    cur.children[ind] = TrieNode()
                cur = cur.children[ind]

            cur.isEnd = True
        
        for word in words:
            insert(word)
        
        found = []
        current = []
        
        def isValid(r, c):
            inBound = 0 <= r < n and 0 <= c < m
            return inBound and not visited[r][c]
        
        def dfs(r, c, curNode):
            if not curNode:
                visited[r][c] = 0
                return
            
            lett = board[r][c]
            ind = ord(lett) - ord("a")
            
            if not curNode.children[ind]:
                visited[r][c] = 0
                return
            
            current.append(lett)
            if curNode.children[ind].isEnd:
                found.append("".join(current))
                curNode.children[ind].isEnd = False
            
            for rOff, cOff in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = r + rOff, c + cOff
                if isValid(nr, nc):
                    visited[nr][nc] = 1
                    dfs(nr, nc, curNode.children[ind])
                    
            visited[r][c] = 0
            current.pop()
        
        for r in range(n):
            for c in range(m):
                visited[r][c] = 1
                dfs(r, c, root)
                
        return found
                