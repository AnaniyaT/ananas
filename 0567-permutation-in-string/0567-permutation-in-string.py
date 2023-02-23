class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        wSize = len(s1)
        target = Counter(s1)
        
        current = Counter(s2[:wSize])
        if current == target:
            return 1
        
        l = 0
        
        for r in range(wSize, len(s2)):
            right = s2[r]
            left = s2[l]
            current[right] = current.get(right, 0) + 1
            
            current[left] -= 1
            if not current[left]:
                current.pop(left)
            l += 1
            
            if current == target:
                return 1
                
        return 0
        