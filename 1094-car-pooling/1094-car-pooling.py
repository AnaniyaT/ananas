class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        locations = [0]*1001
        
        for num, pick, drop in trips:
            locations[pick] += num
            locations[drop] -= num
            
        runSum = 0
        for passengers in locations:
            runSum += passengers
            if runSum > capacity:
                return False
            
        return True