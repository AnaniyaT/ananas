n, k = list(map(int, input().split()))
numbers = list(map(int, input().split()))
numbers = [1]+sorted(numbers)
num = -1
if n == k:
    num = numbers[-1]
elif numbers[k] != numbers[k+1]:
    num = numbers[k]

print(num)