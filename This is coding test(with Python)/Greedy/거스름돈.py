N = int(input()) # 거스름돈
coin = [500, 100, 50, 10] 
result = 0

# i = 0
# while N:
#     result += N // coin[i]
#     N %= coin[i]
#     i += 1

for i in coin:
    result += N // i
    N %= i

print(result)