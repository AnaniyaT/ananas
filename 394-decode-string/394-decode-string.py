class Solution:
    def decodeString(self, s: str) -> str:
        stacknum = []
        stackchar = [""]
        tempnum = 0
        for i in s:
            if i.isnumeric():
                tempnum = (tempnum*10) + int(i)
            elif i == "]":
                temp = stackchar.pop()*stacknum.pop()
                stackchar.append(stackchar.pop()+temp)
            elif i == "[":
                stacknum.append(tempnum)
                stackchar.append("")
                tempnum = 0
            else:
                stackchar[-1] += i
        return stackchar.pop()
                
                