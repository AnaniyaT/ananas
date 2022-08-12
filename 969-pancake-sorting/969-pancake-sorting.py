class Solution:
    def flip(self,listt,k):
        listt = listt[k-1::-1] + listt[k:]
        
    def pancakeSort(self, arr: List[int]) -> List[int]:
        max = len(arr)
        result = []
        r = len(arr)
        while r > 0:
            for i in range(r-1):
                if arr[i] == max:
                    arr = arr[i::-1] + arr[i+1:]
                    result.append(i+1)
                    arr = arr[r-1::-1] + arr[r:]
                    result.append(r)
            max -= 1 
            r -= 1
        return result