import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find_max_rectangle(left: int, right: int):
    if left == right:
        return histogram[left]
    
    mid = (left+right)//2 
    width = 2
    min_height = min(histogram[mid], histogram[mid+1])
    max_ractangle = min_height*width
    
    i = mid; j = mid+1
    while left < i or j < right:
        if j == right or (left < i and histogram[i-1] >= histogram[j+1]):
            i -= 1
            width += 1
            min_height = min(min_height, histogram[i])
            max_ractangle = max(max_ractangle, min_height*width)
        else:
            j += 1
            width += 1
            min_height = min(min_height, histogram[j])
            max_ractangle = max(max_ractangle, min_height*width)
    
    max_ractangle = max(max_ractangle, find_max_rectangle(left, mid), find_max_rectangle(mid+1, right))
    return max_ractangle
    

while True:
    input_values = list(map(int, input().split()))
    n = input_values[0]
    
    if n == 0:
        break
    
    histogram = input_values[1:]
    max_ractangle = find_max_rectangle(0, n-1)
    print(max_ractangle)