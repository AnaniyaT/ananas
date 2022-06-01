class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n = max(nums)
        freqarr = [0]*(n+1)
        for i in nums:
            freqarr[i] += 1
        sortedarr = []
        k=0
        for j in freqarr:
            sortedarr += [k]*j
            k+=1
        result = []
        for l in range (0,len(sortedarr)):
            if sortedarr[l] == target:
                result.append(l)
        return(result)
            
   