# My Solution(72ms)
'''
다음 순열(10972) 문제를 응용해서 풀었다.
다음 순열인 경우 뒷 부분에서 내림차순 정렬의 시작 이전 부분을 찾았다.
이전 순열은 뒷 부분이 오름차순 정렬되어 있어야 하며
오름차순 정렬이 시작되기 전 인덱스를 찾아야 한다.
'''
n = int(input())                                            # 1 ≤ N ≤ 10,000
arr = list(map(int, input().split()))                       # 현재 순열
x = 0                                                       # 오름차순 정렬이 시작되기 전 인덱스
for i in range(n-1, 0, -1):                                 # n-1~1까지 탐색해본다.
    if arr[i] < arr[i-1]:                                   # 만약 이전 원소가 현재 원소보다 크다면 오름차순 정렬에 위반된다.
        x = i-1                                             # x에 i-1을 저장한다.
        break

for i in range(n-1, 0, -1):                                 # n-1~1까지 다시 탐색해본다.
    '''
    뒷 부분은 오름차순 정렬되어 있다.
    따라서 arr[x]가 arr[i]보다 크게 되면 arr[x]보다 작은 값 중 가장 큰 수가 된다.
    해당 원소와 arr[x]를 교체하면 된다.
    '''
    if arr[x] > arr[i]:                                     
        arr[x], arr[i] = arr[i], arr[x]                     
        arr = arr[:x+1] + sorted(arr[x+1:], reverse=True)   # 0~x 까지는 그대로 두고, 이후 부분은 내림차순 정렬한다.
        print(*arr)                         
        exit()

print(-1)


