class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        lol = sorted(intervals)
        output = [lol[0]]
        for i in lol[1:]:
            if i[0] <= output[-1][1]: output[-1][1] = max (output[-1][1],i[1])
            else: output.append(i) 
        return output