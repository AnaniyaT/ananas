class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def isSquare(num):
            return num == (int(num ** 0.5)) ** 2
        
        n = 5000
        prime = [True for i in range(n+1)] 
        p = 2
        while (p * p <= n):  
            if (prime[p] == True): 
                for i in range(p * p, n+1, p): 
                    prime[i] = False
            p += 1
        
        primes = [num for num in range(2, n+1) if prime[num]]
        
        @cache
        def primeFact(num):
            d = num
            
            if num == 1:
                return ()
            
            if num <= 5000 and prime[num]:
                return tuple([num])
            
            for p in primes:
                if not num % p:
                    d = p
                    break
              
            count = 0
            cur = num
            while not cur % d:
                cur //= d
                count += 1
                
            if count % 2:
                return tuple([d, *primeFact(cur)])
            
            return primeFact(cur)
        
        
        p = []
        np = []

        for ind in range(len(nums)):
            if isSquare(ind+1):
                p.append(nums[ind])
            else:
                np.append(ind+1)

        perfects = sum(p)
        n = len(np)
        
        primeFacts = defaultdict(list)

        for idx in np:
            pfact = primeFact(idx)
            primeFacts[tuple(sorted(pfact))].append(idx)
            
        def computeSum(value):
            summ = 0
            for i in value:
                summ += nums[i-1]
                
            return summ
        
        maxx = 0
        for key in primeFacts.keys():
            # print(value)
            if key:
                maxx = max(maxx, computeSum(primeFacts[key]))
            
    
        return max(maxx, perfects)