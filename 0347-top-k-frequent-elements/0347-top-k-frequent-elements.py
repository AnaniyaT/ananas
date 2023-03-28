class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        elements = []
        
        def quickSort(nums):
            pivot = nums[len(nums) // 2]
            freq = frequency[pivot]
            
            left = []
            right = []
            
            for num in nums:
                if num != pivot and frequency[num] >= freq:
                    left.append(num)
                elif num != pivot:
                    right.append(num)
                    
            if len(elements) + len(left) == k - 1:
                left.append(pivot)
                elements.extend(left)
                return
            
            if len(elements) + len(left) > k - 1:
                quickSort(left)
            else:
                left.append(pivot)
                elements.extend(left)
                quickSort(right)
                
        quickSort(list(frequency.keys()))
        
        return elements