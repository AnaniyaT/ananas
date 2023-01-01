class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lettToWord = {}
        wordList = s.split()
        wordSet = set()
        if len(wordList) != len(pattern):
            return False
        
        for ind in range(len(pattern)):
            lett = pattern[ind]
            
            if lett in lettToWord and wordList[ind] != lettToWord[lett]:
                return False
            
            elif not lett in lettToWord:
                word = wordList[ind]
                lettToWord[lett] = word
                wordSet.add(word)
                
        if len(wordSet) != len(lettToWord):
            return False
        
        return True
            
                
        