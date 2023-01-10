class DataStream:

    def __init__(self, value: int, k: int):
        self.k = k
        self.timeSinceValidValue = k
        self.value = value

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.timeSinceValidValue -= 1
        else:
            self.timeSinceValidValue = self.k
        
        if self.timeSinceValidValue < 1:
            return True
        else:
            return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)