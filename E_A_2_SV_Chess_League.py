
n, k = list(map(int, input().split()))

ratings = list(map(int, input().split()))

def possibleWinners(l, r):
    if r - l == 1:
        if abs(ratings[r] - ratings[l]) > k:
            return [max([r, l], key=lambda x: ratings[x])]
        
        return sorted([r, l], key=lambda x: ratings[x])
    
    
    mid = l + (r - l) // 2

    left = possibleWinners(l, mid)
    right = possibleWinners(mid + 1, r)

    leftPtr = rightPtr = 0

    while leftPtr < len(left) and rightPtr < len(right) and abs(ratings[right[rightPtr]] - ratings[left[leftPtr]]) > k:
        if ratings[right[rightPtr]] < ratings[left[leftPtr]]:
            rightPtr += 1   
        else:
            leftPtr += 1
    
    return sorted(left[leftPtr:] + right[rightPtr:], key=lambda x: ratings[x])


result = possibleWinners(0, len(ratings) - 1)

print(*sorted(list(map(lambda x: x + 1, result))))


