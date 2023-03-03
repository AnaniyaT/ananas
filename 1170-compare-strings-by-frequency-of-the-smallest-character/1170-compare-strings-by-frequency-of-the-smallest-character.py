class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def f(s):
            count = Counter(s)
            smallLetter = min(s)
            
            return count[smallLetter]
        
        frequencies = [f(s) for s in words]
        frequencies.sort()
        
        result = []
        numOfWords = len(words)
        
        for query in queries:
            freq = f(query)
            greaterThan = bisect_right(frequencies, freq)
            
            result.append(numOfWords - greaterThan)
            
        return result