class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        smallest = [float('inf'), -1, float('inf'), float('inf')]
        for ind, point in enumerate(points):
            if point[0] == x or point[1] == y:
                manDistance = abs(point[0] - x) + abs(point[1] - y)
                curr = [manDistance, ind, point[0], point[1]]
                if curr < smallest:
                    smallest = curr
        return smallest[1]