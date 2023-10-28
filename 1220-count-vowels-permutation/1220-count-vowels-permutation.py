class Solution:
    def countVowelPermutation(self, n: int) -> int:
        graph = {
            "a": ["e"],
            "e": ["a", "i"],
            "i": ["a", "e", "o", "u"],
            "o": ["i", "u"],
            "u": ["a"]
        }
        
        mod = 10 ** 9 + 7
        
        @cache
        def combs(vowel, level):
            if not level:
                return 1
            
            ans = 0
            for v in graph[vowel]:
                ans += combs(v, level - 1) % mod
            
            return ans % mod
        
        total = 0
        for vowel in "aeiou":
            total += combs(vowel, n-1) % mod
            
        return total % mod
            