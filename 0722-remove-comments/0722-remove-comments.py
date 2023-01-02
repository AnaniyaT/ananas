class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        resultArr = []
        commentFlag = False
        tempLine = []
        
        
        for line in source:
            ignoreInd = -1
            length = len(line)
            for ind, char in enumerate(line):
                if ind == ignoreInd:
                    continue
                if not commentFlag:
                    if char == "/" and ind < length - 1:
                        if line[ind + 1] == "/":
                            if tempLine:
                                lineString = "".join(tempLine)
                                resultArr.append(lineString)
                                tempLine = []  
                            break
                            
                        elif line[ind + 1] == "*":
                            ignoreInd = ind + 1
                            commentFlag = True
                        else:
                            tempLine.append(char)
                    else:
                        tempLine.append(char)
                        
                else:
                    if char == "*" and ind < length - 1 and  line[ind + 1] == "/":
                        ignoreInd = ind + 1
                        commentFlag = False
                        
            if not commentFlag and tempLine:
                lineString = "".join(tempLine)
                resultArr.append(lineString)
                tempLine = []  
                        
            
        return resultArr
                        
            
        
        
                       