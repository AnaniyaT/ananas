class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2!=0:
            return []
        count = collections.Counter(changed)
        ans = []
        for i in sorted(count.keys()):
            if i == 0:
                if count[0]%2!=0:
                    return []
                else:
                    ans+=[0]*int(count[i]/2)
            elif count [i*2] >= count[i]:
                ans += [i]*count[i]
                count[i*2] -= count[i]
            else:
                return []
        return ans