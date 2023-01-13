from collections import defaultdict

testCases = int(input())
for _ in range(testCases):
    nm = input().split()
    rows = int(nm[0])
    cols = int(nm[1])
    diagSum1 = defaultdict(int)
    diagSum2 = defaultdict(int)
    grid = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        grid.append(row)
    
    for row in range(rows):
        for col in range(cols):
            num = grid[row][col]
            diagSum1[row-col] += num
            diagSum2[row+col] += num

    maxx = 0
    for row in range(rows):
        for col in range(cols):
            num = grid[row][col]
            summ = diagSum1[row-col] + diagSum2[row+col] - num
            maxx = max(maxx, summ)

    print (maxx)