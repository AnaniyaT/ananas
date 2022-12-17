class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token[-1].isdigit():
                stack.append(token)
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(str(int(eval(a + token + b))))
        return int(stack[-1])