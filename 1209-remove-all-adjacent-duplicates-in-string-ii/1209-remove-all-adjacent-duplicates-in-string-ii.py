class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = [["0", 0]]
        
        for c in s:
            if c == stk[-1][0]:
                stk[-1][1] += 1
            else:
                stk.append([c, 1])
            
            if stk[-1][1] ==  k:
                stk.pop()
                
        arr = list(map(lambda x: x[0] * x[1], stk))
        
        return "".join(arr)
                