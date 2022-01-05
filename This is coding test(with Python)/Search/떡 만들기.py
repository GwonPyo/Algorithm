n, m = map(int, input().split())
array = list(map(int, input().split()))

left = 0
right = max(array)

result = 0
while left <= right:
    total = 0
    mid = (left + right) // 2

    for x in array:
        if x > mid:
            total += x - mid
    
    if total == m:
        result = mid
        break

    elif total < m:
        right = mid - 1
    
    else:
        result = mid
        left = mid + 1

print(result)