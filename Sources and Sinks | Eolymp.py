n = int(input())

sources = set(range(1, n + 1))
sinks = set(range(1, n + 1))

for fro in range(n):
    line = list(map(int, input().split()))
    for to in range(n):
        if line[to]:
            if fro + 1 in sinks:
                sinks.remove(fro + 1)
            if to + 1 in sources:
                sources.remove(to + 1)

print(len(sources), *sources)
print(len(sinks), *sinks)
