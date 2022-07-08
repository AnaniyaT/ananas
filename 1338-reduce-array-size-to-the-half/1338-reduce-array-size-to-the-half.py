class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = {}
        n = 0
        sum = 0
        for i in arr:
            if i in counter:
                counter[i] +=1
            else:
                counter[i] = 1
        counterlist = sorted(counter, key = counter.get)
        for i in reversed(counterlist):
            if sum  < len(arr)//2:
                sum += counter[i]
                n += 1
            else:
                break
        return n
            
        