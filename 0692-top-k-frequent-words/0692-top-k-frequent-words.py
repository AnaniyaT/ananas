class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        
        counts = [(-freq[word], word) for word in freq]
        heapq.heapify(counts)
        
        topK = []
        for _ in range(k):
            topK.append(heapq.heappop(counts)[1])
            
        return topK