class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        p = 0
        for i in pushed:
            stack.append(i)
            while len(stack) != 0 and stack[-1] == popped[p]:
                stack.pop()
                p += 1
        if len(stack) == 0:
            return True
        return False
            
            