class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        length = len(arr)
        hip = [(arr[length-1], -(length-1))]
        fro, to = 0, 0
        
        for ind in range(len(arr) - 2, -1, -1):
            # print(hip)
            if arr[ind] > hip[0][0]:
                while hip and arr[ind] > hip[0][0]:
                    fro, to = ind, -hip[0][1]
                    heappop(hip)
                break
            
            else:
                heappush(hip, (arr[ind], -ind))
                
        arr[fro], arr[to] = arr[to], arr[ind]
        
        return arr