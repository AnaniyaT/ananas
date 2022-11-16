class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idxmap = {}
        
        for idx, char in enumerate(s):
            idxmap[char] = idx
        
        # not my code it's Dani's he's too proud to submit this "easy" question on his account
        # print(idxmap)
        ans = []
        prev = -1
        partition = 0
        for idx, char in enumerate(s):
            partition = max(partition, idxmap[char])
            if idx == partition:
                ans.append(idx - prev)
                prev = idx
        
        return ans