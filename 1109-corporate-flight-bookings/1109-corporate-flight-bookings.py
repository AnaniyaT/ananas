class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        result = [0]*(n+1)
        for i,j,k in bookings:
            result[i-1] += k
            result[j] -= k
        for i in range(n):
            result[i+1] += result[i]
            
        return result[:n]