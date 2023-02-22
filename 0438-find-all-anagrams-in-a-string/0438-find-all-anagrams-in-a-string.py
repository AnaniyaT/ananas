class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        k = len(p)
        check = Counter(p)
        current = defaultdict(int)
        
        for ind in range(len(s)):
            lett = s[ind]
            current[lett] += 1
            
            if ind >= k:
                leftLett = s[ind-k]
                current[leftLett] -= 1
                if current[leftLett] <= 0:
                    current.pop(leftLett)
                    
            if current == check:
                result.append(ind-k+1)
                
        return result
