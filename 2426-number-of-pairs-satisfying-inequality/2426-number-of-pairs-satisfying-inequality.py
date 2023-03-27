class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        diffArr = [nums1[ind] - nums2[ind] for ind in range(len(nums1))]
        
        pairs = 0
        
        def merge(arr1, arr2):
            nonlocal pairs, diff
            
            merged = []
            p = p1 = p2 = 0
            
            for num in arr2:
                while p < len(arr1) and arr1[p] <= num + diff:
                    p += 1
                
                pairs += p
            
            while p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1] <= arr2[p2]:
                    merged.append(arr1[p1])
                    p1 += 1
                else:
                    merged.append(arr2[p2])
                    p2 += 1
                    
            merged.extend(arr1[p1:])
            merged.extend(arr2[p2:])
            
            return merged
        
        def mergeSort(arr):
            length = len(arr)
            
            if length < 2:
                return arr
            
            mid = length // 2
            
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            
            return merge(left, right)
        
        mergeSort(diffArr)
        
        return pairs