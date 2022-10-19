class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while stack and stack[-1] > i and k:
                stack.pop()
                k -=1 
            stack.append(i)
        if k:
            stack = stack[:-k]
        return(str(int("0"+"".join(stack))))