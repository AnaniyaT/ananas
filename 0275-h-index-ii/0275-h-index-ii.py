class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)
        start, end = 0, length - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if citations[mid] >= length - mid:
                end = mid - 1
            else:
                start = mid + 1 
                
        return length - start