class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        dd = {}
        
        for s, e in flowers:
            dd[s] = dd.get(s, 0) + 1
            dd[e+1] = dd.get(e + 1, 0) - 1
            
        keys = sorted(dd.keys())
        
        for i in range(1, len(keys)):
            dd[keys[i]] += dd[keys[i-1]]
        
        arr = [(key, dd[key]) for key in keys]
        arr.append((float('inf'), 0))
        
        ans = []
    
        for p in people:
            pos = bisect_left(arr, p, key=lambda x: x[0])
            if arr[pos][0] == p:
                ans.append(arr[pos][1])
            else:
                ans.append(arr[pos-1][1])
                
        return ans