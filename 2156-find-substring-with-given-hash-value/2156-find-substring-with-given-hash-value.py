class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        p = 0
        hashh = 0
        
        def v(c):
            return ord(c) - ord("a") + 1
        
        for i in range(n-k, n):
            hashh += v(s[i]) * pow(power, p, modulo)
            hashh %= modulo
            p += 1
    
        start, end = -1, -1
        if hashh == hashValue:
            start, end = n-k, n-1
            
        for ind in range(n-k-1, -1, -1):
            hashh -= v(s[ind+k]) * pow(power, k-1, modulo)
            hashh *= power
            hashh += v(s[ind])
            hashh %= modulo
            if hashh == hashValue:
                start, end = ind, (ind+k-1)
        
        # print(start)
        return s[start:end+1]