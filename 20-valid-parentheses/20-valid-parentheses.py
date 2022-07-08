class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif c == ')' and len(stack) != 0:
                if stack[-1] == '(' :
                    del stack[-1]
                else: return False
            elif c == ']' and len(stack) != 0:
                if stack[-1] == '[':
                    del stack[-1]
                else: return False
            elif c == '}' and len(stack) != 0:
                if stack[-1] == '{':
                    del stack[-1]
                else: return False 
            else: return False
        if len(stack) == 0: return True
        else: return False
        