class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        #Dani's code
        orginal = capacity
        answer = 0
        for idx, plant in enumerate(plants):
            # print(capacity, plant, idx)
            if capacity >= plant:
                answer += 1
                capacity -= plant
            else:
                answer += 2*idx + 1
                capacity = orginal - plant
        
        return answer
            