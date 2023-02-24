def arrayManipulation(n, queries):
    arr = [0]*(n+1)
    
    for query in queries:
        start = query[0] - 1
        end = query[1]
        num = query[2]
        
        arr[start] += num
        arr[end] -= num
        
    runSum = 0
    maxNum = 0
    for ind in range(n):
        runSum += arr[ind]
        maxNum = max(maxNum, runSum)
        
    return maxNum
