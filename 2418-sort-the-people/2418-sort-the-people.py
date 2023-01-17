class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Bubble sort
#         for i in range(len(names)):
#             swaps = 0
#             for ind in range(len(names)-i-1):
#                 if heights[ind] < heights[ind+1]:
#                     heights[ind], heights[ind+1] = heights[ind+1], heights[ind]
#                     names[ind], names[ind+1] = names[ind+1], names[ind]
#                     swaps += 1
                    
#             if not swaps:
#                 break
                
#         return names

        #selection sort
        
#         length = len(names)
        
#         for i in range(length):
#             maxInd = i
#             maxx = 0
#             for ind in range(i, length):
#                 if heights[ind] > maxx:
#                     maxx = heights[ind]
#                     maxInd = ind
            
#             heights[i], heights[maxInd] = heights[maxInd], heights[i]
#             names[i], names[maxInd] = names[maxInd], names[i]
            
#         return names

        # insertion sort
        
#         for i in range(1, len(names)):
#             for ind in range(i-1, -1, -1):
#                 if heights[ind] < heights[i]:
#                     heights[ind], heights[ind+1] = heights[ind+1], heights[ind]
#                     names[ind], names[ind+1] = names[ind+1], names[ind]
#                 else:
#                     break
                    
#         return names

        # counting sort
    
        countArr = [[] for _ in range(max(heights)+1)]
        for ind in range(len(heights)-1, -1, -1):
            countArr[heights[ind]].append(names[ind])
        
        result = []
        for arr in reversed(countArr):
            result.extend(arr)
        
        return result
                