# 최대 공약수, 최소 공배수(기본 for문)
a = 10; b = 12

# 최대 공약수(Greatest common denominator)
for i in range(min(a, b), 0, -1):
    if a%i == 0 and b%i == 0:
        print(i)
        break

# 최소 공배수(Least common multiple)
for i in range(max(a, b), a*b+1):
    if i%a == 0 and i%b == 0:
        print(i)
        break

# 유클리드 호제법
# 최대 공약수
def GCD(x, y):
    while(y):
        x, y = y, x%y
    return x

def LCM(x, y):
    result = (x*y)//GCD(x,y)
    return result

print(GCD(10, 12))
print(LCM(12, 10))

# math 라이브러리
import math

print(math.gcd(10, 12))
print(math.lcm(12, 10))