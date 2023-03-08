class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        indices = [ind for ind in range(len(intervals))]
        
        indices.sort(key=lambda x: intervals[x])
        
        answer = []
        
        for _, end in intervals:
            ind = bisect_left(indices, end, key=lambda x:intervals[x][0])
            
            if ind == len(intervals):
                answer.append(-1)
            else:
                answer.append(indices[ind])
                
        return answer