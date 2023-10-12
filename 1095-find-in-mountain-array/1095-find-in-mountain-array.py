# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain: 'MountainArray') -> int:
        l = 0
        r = mountain.length() - 1
        
        @cache
        def val(ind):
            return mountain.get(ind)
        
        peak = -1
        while l <= r:
            mid = l + (r - l) // 2
            
            prev, midVal, after = val(mid - 1), val(mid), val(mid + 1)
            
            if prev < midVal < after:
                l = mid
            elif after < midVal  < prev:
                r = mid
            else:
                peak = mid
                break
        
        if val(peak) == target:
            return peak
        
        l, r = 0, peak
        
        while l <= r:
            mid = l + (r - l) // 2
            midVal = val(mid)
            
            if midVal < target:
                l = mid + 1
            elif midVal > target:
                r = mid - 1
            else:
                return mid
            
        l, r = peak, mountain.length() - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            midVal = val(mid)
            
            if midVal > target:
                l = mid + 1
            elif midVal < target:
                r = mid - 1
            else:
                return mid
            
        return -1