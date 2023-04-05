class Solution:
    def createSortedArray(self, inst: List[int]) -> int:
        nums = [[0,0] for _ in range(len(inst))]
        
        def merge(arr1, arr2):
            
            p1 = p = p2 = 0
            merged = []
            
            while p1 < len(arr1) and p2 < len(arr2):
                if inst[arr1[p1]] < inst[arr2[p2]]:
                    merged.append(arr1[p1])
                    p1 += 1
                else:
                    while p < len(arr1) and inst[arr1[p]] <= inst[arr2[p2]]:
                        p += 1
                    merged.append(arr2[p2])
                    less = p1
                    greater = len(arr1) - p
                    nums[arr2[p2]][0] += less
                    nums[arr2[p2]][1] += greater
                    p2 += 1
                    
            merged.extend(arr1[p1:])
            while p2 < len(arr2):
                while p < len(arr1) and inst[arr1[p]] <= inst[arr2[p2]]:
                    p += 1
                merged.append(arr2[p2])
                less = p1
                greater = len(arr1) - p
                nums[arr2[p2]][0] += less
                nums[arr2[p2]][1] += greater
                p2 += 1
                
            return merged
        
        def mergeSort(arr):
            if len(arr) < 2:
                return arr
            
            mid = len(arr) // 2
            
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            
            return merge(left, right)
        
        mergeSort([ind for ind in range(len(inst))])

        cost = 0
        for minn, maxx in nums:
            cost += min(minn, maxx)
            
        return cost % 1_000_000_007
            
            
            
            
        