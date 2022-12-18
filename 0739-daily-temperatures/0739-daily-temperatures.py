class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0]*len(temperatures)
        for ind, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                t = stack.pop()
                answer[t[1]] = ind - t[1]
            stack.append((temp, ind))
        return answer