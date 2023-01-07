class Solution:
    def minOperations(self, boxes: str) -> List[int]:
#         # 1st approach - brute force O(n2)
#         answer = [0 for _ in range(len(boxes))]
#         for ind, box in enumerate(boxes):
#             if box == "1":
#                 for indx in range(len(boxes)):
#                     answer[indx] += abs(indx - ind)
        
#         return answer

        # 2nd approach - prefix sum O(n) 2 pass
        
        add = 0
        summ = 0
        answer = [0 for _ in range(len(boxes))]
        
        # forward direction
        for ind, box in enumerate(boxes):
            summ += add
            answer[ind] += summ
            if box == "1":
                add += 1
        
        # backward direction
        add = 0
        summ = 0
        for ind, box in enumerate(reversed(boxes)):
            summ += add
            answer[~ind] += summ
            if box == "1":
                add += 1
                
        return answer
                
        