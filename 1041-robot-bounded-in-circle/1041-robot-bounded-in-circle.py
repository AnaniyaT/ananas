class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        d = (0, 1)
        cur = [0, 0]
        
        instructions = instructions * 4
        for inst in instructions:
            if inst == "G":
                cur[0] += d[0]
                cur[1] += d[1]
            elif inst == "L":
                d = (-d[1], d[0])
            else:
                d = (d[1], -d[0])
                
        return cur == [0, 0]