class Solution:
    def splitString(self, s: str) -> bool:
        curr = []
        length = len(s)
        
        def backtrack(ind):
            nonlocal length, s
            
            if ind >= length:
                return len(curr) > 1
            
            for end in range(ind+1, length+1):
                val = int(s[ind:end])
                
                if not curr or val == curr[-1] - 1:
                    curr.append(val)

                    if backtrack(end):
                        return True
                    
                    curr.pop()
                    
            return False
                    
        return backtrack(0)  
           
                    
                    