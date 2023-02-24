class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token not in ["*", "-", "+", "/"]:
                stack.append(token)
            else:
                operation = token
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(str(int(eval(num1+operation+num2))))
                
        return int(stack[-1])
                