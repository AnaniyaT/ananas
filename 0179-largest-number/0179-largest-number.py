class Solution:
    def compare(self, num1, num2):
        if int(num1+num2) < int(num2+num1):
            return 1
        else:
            return -1
        
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(self.compare))
        return str(int("".join(nums)))
            
        