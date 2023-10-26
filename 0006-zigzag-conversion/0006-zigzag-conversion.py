class Solution:
    def convert(self, s: str, numRows: int) -> str:
        numRows = min(numRows, len(s))
        
        rows = [[] for _ in range(numRows)]
        order = [i for i in range(numRows)] + [i for i in range(numRows-2, 0, -1)]
        mod = len(order)
        
        for idx, c in enumerate(s):
            row = order[idx % mod]
            rows[row].append(c)
            
        newWord = []
        for row in rows:
            newWord.extend(row)
        
        return "".join(newWord)
        
        
        