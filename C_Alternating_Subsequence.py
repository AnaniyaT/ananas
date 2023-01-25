tests = int(input())
for _ in range(tests):
    length = int(input())
    maxPos = 0
    maxNeg = -float("inf")
    maxSum = 0
    pos = True
    nums = list(map(int, input().split()))
    for num in nums:
        if pos:
            if num < 0:
                maxSum += maxPos
                pos = False
                maxNeg = num
            else:
                maxPos = max(maxPos, num)
        else:
            if num > 0:
                maxSum += maxNeg
                pos = True
                maxPos = num
            else:
                maxNeg = max(maxNeg, num)
    
    if pos:
        maxSum += maxPos
    else:
        maxSum += maxNeg
    
    print (maxSum)
