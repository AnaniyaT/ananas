class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first = edges[0]
        secnd = edges[1]
        
        if first[0] in secnd:
            return first[0]
        
        return first[1]