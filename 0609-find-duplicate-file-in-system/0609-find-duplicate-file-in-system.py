class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contentDict = defaultdict(list)
        
        for path in paths:
            directory = path.split(" ", maxsplit=1)
            parent = directory[0]+"/"
            fileList = []
            contentList = []
           
            #boolean parenthesis Flag to know if a parenthesis has been opened
            pFlag = False
            
            if len(directory) > 1:
                for char in directory[1]:
                    if char == "(":
                        pFlag = True
                        
                    elif char == ")":
                        content = "".join(contentList)
                        file = "".join(fileList)
                        contentDict[content].append(parent+file)
                        pFlag = False
                        
                        fileList = []
                        contentList = []
                        
                    elif char != " ":
                        if pFlag:
                            contentList.append(char)
                        else:
                            fileList.append(char)
                    
            
                            
        result = []
        for contentt in contentDict:
            dirs = contentDict[contentt]
            if len(dirs) > 1:
                result.append(contentDict[contentt])

        return result
                        