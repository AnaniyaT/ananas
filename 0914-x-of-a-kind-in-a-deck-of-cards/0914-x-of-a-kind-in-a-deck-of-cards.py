class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        
        gcd = 0
        for key in count:
            gcd = math.gcd(gcd, count[key])
            
        return gcd > 1