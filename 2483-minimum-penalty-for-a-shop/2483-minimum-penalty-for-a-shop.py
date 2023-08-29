class Solution:
    def bestClosingTime(self, customers: str) -> int:
        customers = customers + "N"
        n = len(customers)
        count = Counter(customers)["Y"]
        minn = float('inf')
        minInd = 0
        sofar = 0
        
        for ind in range(n):
            penalty =  (ind - sofar) + count
            if penalty < minn:
                minInd = ind
                minn = penalty
                
            if customers[ind] == "Y":
                sofar += 1
                count -= 1
                
        return minInd