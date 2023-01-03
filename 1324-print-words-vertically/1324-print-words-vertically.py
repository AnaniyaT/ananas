class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        maxLen = max([len(word) for word in s])
        output = [[] for _ in range(maxLen)]
        for word in s:
            for ind, char in enumerate(word):
                output[ind].append(char)
            for indx in range(ind + 1, maxLen):
                output[indx].append(" ")
        
        # To get rid of trailing spaces
        for word in output:
            while word[-1] == " ":
                word.pop()
                
        output = ["".join(word) for word in output]
        
        return output
        
        
        