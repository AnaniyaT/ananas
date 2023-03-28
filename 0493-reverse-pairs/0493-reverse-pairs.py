class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        pairs = 0
        
        def merge(arr1, arr2):
            nonlocal pairs
            
            p = p1 = p2 = 0
            merged = []
            
            while p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1] < arr2[p2]:
                    merged.append(arr1[p1])
                    p1 += 1
                else:
                    while p < len(arr1) and arr1[p] <= 2 * arr2[p2]:
                        p += 1
                    
                    pairs += len(arr1) - p
                    merged.append(arr2[p2])
                    p2 += 1
                    
            merged.extend(arr1[p1:])
            
            while p2 < len(arr2):
                while p < len(arr1) and arr1[p] <= 2 * arr2[p2]:
                    p += 1

                pairs += len(arr1) - p
                merged.append(arr2[p2])
                p2 += 1
            
            
            return merged
            
        def mergeSort(arr):
            if len(arr) < 2:
                return arr
            
            mid = len(arr) // 2
            
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            
            return merge(left, right)
        
        mergeSort(nums)
        
        return pairs
            