class Solution:
    def smallestNumber(self, pattern: str) -> str:
        pattern = list(pattern)
        
        pattern.append(pattern[-1])
        
        stack = []
        
        n = 1
        for ind, p in enumerate(pattern):
            if p == "I":
                pattern[ind] = str(n)
                n += 1
                while stack:
                    pattern[stack.pop()] = str(n)
                    n += 1
                    
            else:
                stack.append(ind)
                
        while stack:
            pattern[stack.pop()] = str(n)
            n += 1
            
        return "".join(pattern)
                    
                
        
               