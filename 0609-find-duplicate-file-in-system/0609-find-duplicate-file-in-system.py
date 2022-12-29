class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contentDict = defaultdict(list)
        for path in paths:
            splitPath = path.split()
            parent = splitPath[0] + "/"
            
            for file in splitPath[1:]:
                splitFile = file.split("(")
                fileName = splitFile[0]
                content = splitFile[1][:-1]
                
                contentDict[content].append(parent + fileName)
        
        result = []
        for contentt in contentDict:
            duplicates = contentDict[contentt]
            if len(duplicates) > 1:
                result.append(duplicates)
                
        return result