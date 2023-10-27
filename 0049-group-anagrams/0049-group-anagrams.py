class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        sortedStrs = []
        
        for s in strs:
            sortedStrs.append("".join(sorted(s)))
            
        groups = defaultdict(list)
        
        for idx in range(n):
            string = strs[idx]
            rep = sortedStrs[idx]
            
            groups[rep].append(string)
            
        return groups.values()
            