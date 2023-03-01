class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        closeInd = [ind for ind in range(len(position))]
        closeInd.sort(key=lambda x: position[x], reverse=True)
        
        stack = []
        for ind in closeInd:
            timeTaken = (target-position[ind])/speed[ind]
            if not stack or timeTaken > stack[-1]:
                stack.append(timeTaken)
            
        return len(stack)