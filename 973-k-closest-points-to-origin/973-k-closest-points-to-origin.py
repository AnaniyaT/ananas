class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
                
        
        x = lambda a : int(a[0]**2)+(a[1]**2)
        arr = []
        result = []
        for i in points:
            s = x(i)
            arr.append([s,i])
        heapq.heapify(arr)
        for j in range (k):
            result.append(arr[0][1])
            heapq.heappop(arr)
                
        return result