class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = [0] * len(nums)
        nums = [(ind, num) for ind, num in enumerate(nums)]
        
        def merge(arr1, arr2):
            p1 = p2 = 0
            
            merged = []
            while p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1][1] <= arr2[p2][1]:
                    merged.append(arr1[p1])
                    counts[arr1[p1][0]] += p2
                    p1 += 1
                else:
                    merged.append(arr2[p2])
                    p2 += 1
                    
            while p1 < len(arr1):
                merged.append(arr1[p1])
                counts[arr1[p1][0]] += p2
                p1 += 1
                
            merged.extend(arr2[p2:])
            
            return merged
            
        def mergeSort(arr):
            if len(arr) < 2:
                return arr
            
            mid = len(arr) // 2
            
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            
            return merge(left, right)
        
        mergeSort(nums)
        
        return counts
                    