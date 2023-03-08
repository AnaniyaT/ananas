tests = int(input())

# for _ in range(tests):
#     a, b = map(int, input().split())

#     print(min(a, b, (a+b)//4))

for _ in range(tests):
    a, b = map(int, input().split())

    start = min(a, b)
    end = (a + b) // 4

    while start <= end:
        mid = start + (end - start) // 2

        if mid <= min(a, b) and mid * 4 <= a + b:
            start = mid + 1
        else:
            end = mid - 1

    print(end)

