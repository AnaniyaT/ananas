class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = [0] * 26
        
        for char in s:
            ind = ord("z") - ord (char)
            count[ind] += 1
        
        result = []
        
        for ind in range(26):
            nextInd = ind + 1
            while count[ind]:
                times = min(count[ind], repeatLimit)
                result.extend([chr(ord("z") - ind)] * times)
                count[ind] -= times
                
                if nextInd == 26:
                    return "".join(result)
                
                if count[ind]:
                    while nextInd < 26 and not count[nextInd]:
                        nextInd += 1
                    
                    if nextInd == 26:
                        return "".join(result)
                    
                    result.append(chr(ord("z") - nextInd))
                    count[nextInd] -= 1
                    
        return "".join(result)
                        
        