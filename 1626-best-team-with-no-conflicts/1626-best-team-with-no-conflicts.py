class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        indices = sorted([i for i in range(n)], key=lambda x:(ages[x], scores[x]))
        
        maxSums = [scores[indices[i]] for i in range(n)]
        
        for i, ind in enumerate(indices):
            num = scores[ind]
            for j in range(i):
                num1 = scores[indices[j]]
                if num1 <= num:
                    maxSums[i] = max(maxSums[i], num + maxSums[j])
        
        # print(maxSums)
        return max(maxSums)