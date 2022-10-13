class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        listt = [0]*1001
        summ = 0
        for i,j,k in trips:
            listt[j] += i
            listt[k] -= i
        for i in listt:
            summ += i
            if summ > capacity:
                return False
        return True