class Solution:
    def splitString(self, s: str) -> bool:
        slices = []
        found = False
        
        def check():
            if len(slices) < 2:
                return False
            
            if int(slices[-2]) - int(slices[-1]) != 1:
                return False
                
            return True
        
        
        def backtrack(strg):
            nonlocal found
            
            if found:
                return
            
            if not strg:
                if check():
                    found = True
                return
            
            n = len(strg)
            
            for i in range(1, n+1):
            
                slices.append(strg[:i])
                
                if len(slices) > 1:
                    first = int(slices[-2])
                    second = int(slices[-1])
                    
                    if first - second != 1:
                        slices.pop()
                        continue
                
                backtrack(strg[i:])
    
                slices.pop()
                
                
        backtrack(s)
        
        return found
                
            