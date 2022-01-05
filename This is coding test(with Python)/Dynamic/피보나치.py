array = [0, 1, 1] + [None] * 98
n = int(input())

# def fibo(n):
#     if array[n] == None:
#         return fibo(n - 1) + fibo(n - 2)
    
#     else:
#         return array[n]

def fibo(n):
    for i in range(3, n + 1):
        if array[i] == None:
            array[i] = array[i - 1] + array[i - 2]
    
    return array[n]
            

print(fibo(n))