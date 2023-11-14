class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        palis = [[0] * 26 for _ in range(26)]
        
        def idx(ch):
            return ord(ch) - ord("a")
        
        counts = [0 for _ in range(26)]
        for ch in s:
            counts[idx(ch)] += 1
        
        curCount = [0 for _ in range(26)]
        curCount[idx(s[0])] += 1
        counts[idx(s[0])] -= 1
        
        for ind in range(1, n-1):
            c = idx(s[ind])
            counts[c] -= 1
            for let in range(26):
                if counts[let] and curCount[let]:
                    palis[c][let] = 1
                    
            curCount[c] += 1
            
        return sum([sum(row) for row in palis])