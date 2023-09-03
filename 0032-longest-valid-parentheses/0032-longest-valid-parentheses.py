class Solution:
    def longestValidParentheses(self, s: str) -> int:
        valids = [0 for _ in range(len(s) + 1)]
        ends = []
        
        stak = []
        for ind, p in enumerate(s):
            if p == "(":
                stak.append(ind)
            else:
                if stak:
                    start = stak.pop()
                    valids[ind] = ind - start + 1
                    ends.append(ind)
                else:
                    prev = 0
                    
        maxx = 0
        for ind in ends:
            valids[ind] += valids[ind - valids[ind]]
            maxx = max(maxx, valids[ind])
            
        return maxx
                
            