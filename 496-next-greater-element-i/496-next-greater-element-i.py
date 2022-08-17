class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        result = []
        for i in nums1:
            n = nums2.index(i)+1
            while True:
                if n == len(nums2):
                    result.append(-1)
                    break
                if nums2[n] > i:
                    result.append(nums2[n])
                    break
                    n += 1
                else:
                    n += 1
        return result