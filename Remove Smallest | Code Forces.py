tests = int(input())
for _ in range(tests):
    length = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    delCount = 0
    for ind in range(length-1):
        if arr[ind+1] - arr[ind] <= 1:
            delCount += 1

    if delCount == length-1:
        print("YES")
    else:
        print("NO")
