class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for p in s:
            if p == "(":
                stack.append(0)
            elif p == ")" and stack[-1]:
                temp = 0
                
                while stack and stack[-1]:
                    temp += stack.pop()
                    
                stack[-1] += (2*temp)
                
            else:
                stack[-1] += 1
                        
        return sum(stack)