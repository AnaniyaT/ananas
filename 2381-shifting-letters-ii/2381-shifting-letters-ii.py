class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shiftsSum = [0]*(len(s)+1)
        
        for shift in shifts:
            start = shift[0]
            end = shift[1]
            direction = shift[2]
            if direction:
                shiftsSum[start] += 1
                shiftsSum[end+1] -= 1
            else:
                shiftsSum[start] -= 1
                shiftsSum[end+1] += 1
            
        result = []
        summ = 0
       
        for ind, char in enumerate(s):
            summ += shiftsSum[ind]
            letter = chr(ord('a') + (ord(char) - ord('a') + summ)%26)
            result.append(letter)
            
        return "".join(result)