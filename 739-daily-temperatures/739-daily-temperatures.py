class Solution(object):
    def dailyTemperatures(self, temperatures):
        result = [0]*len(temperatures)
        stack = []
        for i,j in enumerate(temperatures):
            while stack and stack[-1][-1] < j:
                temp = stack.pop()
                result[temp[0]] = i-temp[0]
            stack.append([i,j])
        return result