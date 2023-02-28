class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if not rowIndex:
            return [1]
        
        before = self.getRow(rowIndex-1)
        before.append(0)
        
        result = []
        for ind in range(rowIndex+1):
            current = before[ind] + before[ind-1]
            result.append(current)
            
        return result