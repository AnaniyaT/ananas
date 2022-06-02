class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key = lambda a: int(a),reverse = True)
        return (nums[k-1])
        
        