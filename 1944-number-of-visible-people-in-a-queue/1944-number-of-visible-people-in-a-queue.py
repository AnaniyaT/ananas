class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        length = len(heights)
        result = [0] * length
        stack = []

        for ind, height in enumerate(reversed(heights)):
            people = 0
            while stack and stack[-1] < height:
                people += 1
                stack.pop()
            if stack:
                people += 1

            stack.append(height)
            result[~ind] = people

        return result