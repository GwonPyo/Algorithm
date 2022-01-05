import sys
input = sys.stdin.readline

def binary_search(array, target):
    pl = 0
    pr = len(array) - 1

    while pl <= pr:
        pm = (pl + pr) // 2
        if array[pm] == target:
            return 'yes'
        elif array[pm] > target:
            pr = pm - 1
        else:
            pl = pm + 1

    return 'no'

n = int(input())
stock_list = list(map(int, input().split()))
stock_list.sort()

m = int(input())
check_list = list(map(int, input().split()))

result = []
for check_num in check_list:
    result.append(binary_search(stock_list, check_num))

print(' '.join(result))

