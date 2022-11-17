class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        lengthA, lengthB = ay2 - ay1, by2 - by1
        widthA, widthB = ax2 - ax1, bx2 - bx1
        areaOfRectA = lengthA * widthA
        areaOfRectB = lengthB * widthB
        
        if max(ax1, bx1) < min(ax2, bx2) and max(ay1, by1) < min(ay2, by2):
            overlapLength = min(by2, ay2) - max(ay1, by1)
            overlapWidth = min(ax2, bx2) - max(bx1, ax1)
            return (areaOfRectA + areaOfRectB) - (overlapLength*overlapWidth)
        
        return areaOfRectA+areaOfRectB