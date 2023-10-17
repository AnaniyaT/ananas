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
            facts = []
            isBigPrime = True
            for p in primes:
                if p > num:
                    break
                while not num % p:
                    isBigPrime = False
                    facts.append(p)
                    num //= p
                    
            if isBigPrime:
                return None
                    
            counts = Counter(facts)
            return tuple([(p, counts.get(p, 0) % 2) for p in primes if counts.get(p, 0) % 2])
        
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
            primeFacts[pfact].append(idx)
            
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