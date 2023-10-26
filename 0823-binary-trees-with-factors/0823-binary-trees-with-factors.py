class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        mod = 10 ** 9 + 7
        n = len(arr)
        
        trees = n
        ways = [1 for _ in range(n)]
        
        for idx in range(n):
            cur = arr[idx]
            nums = defaultdict(lambda : -1)
            
            for ind in range(idx+1):
                num = arr[ind]
                nums[num] = ind
                tar = -1 if cur % num else cur // num
                
                if nums[tar] != -1:
                    way = ways[nums[tar]] * ways[ind]
                    if num != tar:
                        way *= 2
                    
                    ways[idx] += way
        
        return sum(ways) % mod
                
                