class Solution:
    @cache
    def longestCommonSubsequence(self, text1, text2):
        if len(text1) == 0 or len(text2) == 0:
            return 0
        if text1[0] == text2[0]:
            return 1 + self.longestCommonSubsequence(text1[1:],text2[1:])
        else:
            return max(self.longestCommonSubsequence(text1,text2[1:]), self.longestCommonSubsequence(text1[1:],text2))
        