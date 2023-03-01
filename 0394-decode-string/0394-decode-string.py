class Solution:
    def decode(self, string):
        num = braces = 0
        chars = []
        temp = []
        
        for char in string:
            if char.isdigit() and not braces:
                num = num*10 + int(char)
            elif char == "[":
                if braces:
                    temp.append(char)
                braces += 1
            elif char == "]":
                braces -= 1
                if braces:
                    temp.append(char)
                else:
                    chars.extend(num*self.decode(temp))
                    num = 0
                    temp = []
            elif braces:
                temp.append(char)
            else:
                chars.append(char)
        
        return chars
                    
                
    def decodeString(self, s: str) -> str:
        resultList = self.decode(list(s))
        
        return "".join(resultList)