class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        numIndx = {}
        for i,j in enumerate(nums1):
            numIndx[j] = i
        stack = []
        result = [-1]*len(nums1)
        for num in nums2:
            while stack and stack[-1] < num:
                result[numIndx[stack.pop()]] = num
            if num in numIndx:
                stack.append(num)
        return result