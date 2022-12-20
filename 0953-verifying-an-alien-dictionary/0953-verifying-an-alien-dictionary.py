class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphaMap = {}
        for ind, letter in enumerate(order):
            alphaMap[letter] = ind
        def compare(word1, word2):
            for ind in range(min(len(word1), len(word2))):
                if alphaMap[word1[ind]] < alphaMap[word2[ind]]:
                    return True
                if alphaMap[word1[ind]] > alphaMap[word2[ind]]:
                    return False
            if len(word1) <= len(word2):
                return True
            return False
              
        for ind in range(len(words)-1):
            if not compare(words[ind], words[ind+1]):
                return False
        return True
            
        
        