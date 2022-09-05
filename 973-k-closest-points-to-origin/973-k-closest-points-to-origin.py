class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        x = lambda a : (a[0]**2)+(a[1]**2)
        points = sorted(points,key = x)
        return points[:k]
    