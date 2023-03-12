class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        opened = 0
        lonelies = 0
        
        for ch in s:
            if ch == "(":
                opened += 1
                
            elif ch == ")":
                if opened:
                    opened -= 1
                else:
                    lonelies += 1
        
        minRemove = opened + lonelies
        
        if not minRemove:
            return [s]
        
        if minRemove == len(s):
            return [""]
        
        def check(sequence):
            opened = 0
            
            for ch in sequence:
                if ch == "(":
                    opened += 1
                    
                elif ch == ")":
                    if not opened:
                        return False
                    opened -= 1
            
            if opened:
                return False
            
            return True
        
        answer = set()
        sequence = list(s)
        
        def backtrack(rem, ind):
            if not rem or ind == len(sequence):
                return
                
            if sequence[ind] in ["(",")"]:
                char = sequence[ind]
                sequence[ind] = ""
                
                if check(sequence):
                    answer.add("".join(sequence))

                backtrack(rem - 1, ind + 1)
                
                sequence[ind] = char
                
            backtrack(rem, ind + 1)
        
        
        backtrack(minRemove, 0)
        
        return list(answer)
        
        