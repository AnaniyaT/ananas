n = int(input())

roads = 0

for r in range(n):
    line = input().split()
    for c in range(r + 1, n):
        if line[c] == "1":
            roads += 1
            
print(roads)
