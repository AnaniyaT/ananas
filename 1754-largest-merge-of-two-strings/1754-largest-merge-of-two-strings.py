class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merged = []
        p = 0
        for ind in range(len(word1)):
            while p < len(word2) and word1[ind:] < word2[p:]:
                merged.append(word2[p])
                p += 1
            merged.append(word1[ind])
            
        while p < len(word2):
            merged.append(word2[p])
            p += 1
        
        return "".join(merged)