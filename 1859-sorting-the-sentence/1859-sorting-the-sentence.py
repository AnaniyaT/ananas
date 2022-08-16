class Solution:
    def sortSentence(self, s: str) -> str:
        wordList = s.split(" ")
        sentenceList = [""]*len(wordList)
        for word in wordList:
            sentenceList[int(word[-1])-1] = word[:-1]
        return " ".join(sentenceList)