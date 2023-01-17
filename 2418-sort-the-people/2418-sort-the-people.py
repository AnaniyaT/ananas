class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)):
            for ind in range(len(names)-i-1 ):
                if heights[ind] < heights[ind+1]:
                    heights[ind], heights[ind+1] = heights[ind+1], heights[ind]
                    names[ind], names[ind+1] = names[ind+1], names[ind]
        
        return names