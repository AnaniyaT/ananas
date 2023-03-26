class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        length = len(dominoes)
        inf = float('inf')
        
        distances = [[inf, inf] for _ in range(length)]
        
        r = -inf
        stack = []
        for ind, dom in enumerate(dominoes):
            if dom == "L":
                r = -inf
                distances[ind][0] = 0
                while stack:
                    indx = stack.pop()
                    distances[indx][0] = ind - indx
                    
            elif dom == "R":
                stack = []
                r = ind
                
            else:
                stack.append(ind)
                
            distances[ind][1] = ind - r
            
        result = []
        for distance in distances:
            ld, rd = distance
            if ld < rd:
                result.append("L")
            elif rd < ld:
                result.append("R")
            else:
                result.append(".")
    
        return "".join(result)
            