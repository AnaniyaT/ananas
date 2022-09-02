class Solution:
    def calculate(self, s: str) -> int:
        ss = []
        temp = ""
        for ch in s:
            if ch != " ":
                if ch in ["+","-","/","*"]:
                    ss.append(temp)
                    ss.append(ch)
                    temp = ""
                else:
                    temp += ch
        ss.append(temp)
        stack = []
        i = 0
        while i < len(ss):
            if ss[i] == "/":
                stack.append(int(int(stack.pop())/int(ss[i+1])))
                i += 2
            elif ss[i] == "*":
                stack.append((int(stack.pop())*int(ss[i+1])))
                i += 2
            else:
                stack.append(ss[i])
                i += 1
        ss = stack
        stack = []
        i = 0

        while i < len(ss):
            if ss[i] == "-":
                stack.append(int(int(stack.pop())-int(ss[i+1])))
                i += 2
            elif ss[i] == "+":
                stack.append(int(int(stack.pop())+int(ss[i+1])))
                i += 2
            else:
                stack.append(ss[i])
                i += 1
        return int(stack[-1])


                             