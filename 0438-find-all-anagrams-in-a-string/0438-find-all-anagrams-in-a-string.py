class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        k = len(p)
        check = Counter(p)
        
        for ind in range(len(s)):
            lett = s[ind]
            if lett in check:
                check[lett] -= 1
                
            if ind >= k:
                leftLett = s[ind-k]
                if leftLett in check:
                    check[leftLett] += 1
                    
            if all(x == 0 for x in check.values()):
                result.append(ind-k+1)
            

        return result
