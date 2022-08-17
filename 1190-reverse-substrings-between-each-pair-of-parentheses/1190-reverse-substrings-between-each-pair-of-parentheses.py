class Solution(object):
    def reverseParentheses(self, s):
        stack = [""]
        for i in s:
            if i == "(":
                stack.append("")
            elif i == ")":
                temp = stack.pop()[::-1]
                stack[-1] += temp
            else:
                stack[-1] += i
        return stack[-1]
        