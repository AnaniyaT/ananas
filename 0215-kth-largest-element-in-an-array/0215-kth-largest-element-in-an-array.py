class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSort(l, arr):
            nonlocal k
            
            left = []
            right = []
            
            pivot = len(arr) // 2
            
            for ind, num in enumerate(arr):
                if ind != pivot and num > arr[pivot]:
                    left.append(num)
                elif ind != pivot:
                    right.append(num)
                    
            if l + len(left) == k - 1:
                return arr[pivot]
            
            if l + len(left) < k - 1:
                return quickSort(l + len(left) + 1, right)
            else:
                return quickSort(l, left)
                
        return quickSort(0, nums)