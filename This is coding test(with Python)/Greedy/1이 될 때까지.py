N, K = map(int, input().split())
# N: 연산 대상
# K: 나눌 수 있는 수

count = 0

# while N >= 1:
#     if N % K != 0:
#         N -= 1
    
#     else:
#         N //= K
#     count += 1

while True:
    target = (N // K) * K
    count += N - target
    N = target

    if N < K:
        break
    
    N //= K
    count += 1

count += (N - 1)
print(count)