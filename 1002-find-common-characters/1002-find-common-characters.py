class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        lettArr = [100 for _ in range(26)]
        for word in words:
            tempArr = [0 for _ in range(26)]
            for char in word:
                ind = ord(char) - ord("a")
                tempArr[ind] += 1
            
            for ind in range(26):
                lettArr[ind] = min(lettArr[ind], tempArr[ind])
        
        answer = []
        for ind, lett in enumerate(lettArr):
            for _ in range(lett):
                answer.append(chr(ind + ord("a")))
        
        return answer
            