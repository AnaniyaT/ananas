class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return Counter(bin(x ^ y))["1"]