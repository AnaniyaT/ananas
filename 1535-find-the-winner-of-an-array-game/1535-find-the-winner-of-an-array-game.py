class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        arr = arr[::-1]
        
        streak = 0
        prev = 0
        
        while len(arr) > 1:
            mx = max(arr.pop(), arr.pop())
            
            if mx == prev:
                streak += 1
            else:
                prev = mx
                streak = 1
            
            if streak == k:
                return mx
            
            arr.append(mx)
            
        return arr[0]
        