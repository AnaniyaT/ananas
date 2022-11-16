class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        currCap = capacity
        for i, j in enumerate(plants):
            if currCap >= j:
                steps += 1
                currCap -= j
            else:
                steps += 2*i+1
                currCap = capacity - j
        return steps
            