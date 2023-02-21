lengths = input()
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

combined = []
p = 0

for num in arr1:
    while p < len(arr2) and arr2[p] < num:
        combined.append(arr2[p])
        p += 1
    combined.append(num)

combined.extend(arr2[p:])

print(*combined)
