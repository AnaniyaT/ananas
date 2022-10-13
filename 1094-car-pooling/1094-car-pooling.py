class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        count = 0
        dest = []
        for i,j,k in sorted(trips, key = lambda a: a[1]):
            count += i
            heappush(dest, (k,i))
            while dest[0][0] <= j:
                count -= heappop(dest)[1]
            if count > capacity:
                return False
        return True