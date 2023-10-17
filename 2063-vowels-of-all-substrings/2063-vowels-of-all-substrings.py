class Solution:
    def countVowels(self, word: str) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        n = len(word)
        subs = 0
        
        for indx in range(n):
            c = word[indx]
            
            if c in vowels:
                l = indx + 1
                r = n - indx
                subs += l * r
                
        return subs
                