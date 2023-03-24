class Solution:
    def maxLength(self, arr: List[str]) -> int:
        curr = []
        length = len(arr)
        maxLen = 0
        
        def backtrack(ind):
            nonlocal maxLen, length
            
            if ind == length:
                return
            
            string = arr[ind]
            pos = True
            
            for indx, char in enumerate(string):
                if char not in curr:
                    curr.append(char)
                else:
                    for _ in range(indx):
                        curr.pop()
                    pos = False
                    break
            
            maxLen = max(maxLen, len(curr))
            
            if pos:
                backtrack(ind + 1)

                for _ in range(len(string)):
                    curr.pop()
                
            backtrack(ind + 1)
            
        backtrack(0)
        
        return maxLen
        