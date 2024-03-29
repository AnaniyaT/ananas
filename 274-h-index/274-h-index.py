class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse = True)
        for i,j in enumerate(citations):
            if i >= j:
                return i
        return len(citations)