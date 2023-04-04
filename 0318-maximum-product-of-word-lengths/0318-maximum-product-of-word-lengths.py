class Solution:
    def maxProduct(self, words: List[str]) -> int:
        lettUsed = []
        
        for word in words:
            letters = 0
            for lett in word:
                shift = ord(lett) - ord('a')
                mask = 1 << shift
                
                letters |= mask
                
            lettUsed.append(letters)
            
        maxVal = 0
        
        for i in range(len(lettUsed)):
            for j in range(i+1, len(lettUsed)):
                if not lettUsed[i] & lettUsed[j]:
                    prod = len(words[i]) * len(words[j])
                    maxVal = max(maxVal, prod)
            
        return maxVal