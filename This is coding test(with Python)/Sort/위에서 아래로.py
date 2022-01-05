n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

array.sort(reverse = True)
print(*array)