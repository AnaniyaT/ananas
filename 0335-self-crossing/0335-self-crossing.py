class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        def isCrossed(v1, v2):
            v1x1, v1y1, v1x2, v1y2 = v1
            v2x1, v2y1, v2x2, v2y2 = v2
            
            v1Ver = v1x1 == v1x2
            v2Ver = v2x1 == v2x2
            
            if v1Ver and v2Ver:
                if not v1x1 == v2x1:
                    return False
                
                return min(max(v1y1, v1y2), max(v2y1, v2y2)) >= max(min(v1y1, v1y2), min(v2y1, v2y2))
            
            if not v1Ver and not v2Ver:
                if not v1y1 == v2y1:
                    return False
                
                return min(max(v1x1, v1x2), max(v2x1, v2x2)) >= max(min(v1x1, v1x2), min(v2x1, v2x2))
            
            if not v1Ver and v2Ver:
                cond1 = min(v1x1, v1x2) <= v2x1 <= max(v1x1, v1x2)
                cond2 = min(v2y1, v2y2) <= v1y1 <= max(v2y1, v2y2)
                
                return cond1 and cond2
            
            else:
                cond1 = min(v2x1, v2x2) <= v1x1 <= max(v2x1, v2x2)
                cond2 = min(v1y1, v1y2) <= v2y1 <= max(v1y1, v1y2)
                
                return cond1 and cond2
            
        
        lines = deque()
        lastx, lasty = 0, 0
        
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        for ind, s in enumerate(distance):
            d = ind % 4
            
            curx, cury = (lastx + dirs[d][0] * s, lasty + dirs[d][1] * s)
            curLine = (lastx, lasty, curx, cury)
            for idx in range(max(0, len(lines) - 2)):
                if isCrossed(lines[idx], curLine):
                    # print(idx, lines[idx], curLine)
                    return True
                
            lines.append(curLine)
            lastx, lasty = curx, cury
            if len(lines) > 5:
                lines.popleft()
        
        return False
        