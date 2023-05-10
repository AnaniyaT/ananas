class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        while len(matrix) > 1:
            matrix[0].extend(matrix.pop())
            
        heapify(matrix[0])
        
        for _ in range(k-1):
            heappop(matrix[0])
            
        return matrix[0][0]