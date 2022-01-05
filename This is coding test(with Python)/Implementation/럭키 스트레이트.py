'''
풀이 시간: 5분
기술을 쓰러면 점수 n을 자릿수를 기준으로 반을 나누어, 
왼쪽 부분과 오른쪽 부분의 각 자릿수의 합이 같아야 한다.
따라서 n을 문자열로 나두고 슬라이싱을 이용해 반으로 나눠준다.
그리고 리스트로 만들어 수를 각 숫자로 나누고 map을 이용해 int형으로 바꾼다.
이후 sum() 함수를 이용해 총 합을 구하고 같은지 확인하여 LUCKY 혹은 READY를 출력하면 된다.
'''
n = input() # 점수 n

# 앞뒤로 나눠준다.
# 조건에 N의 자릿수는 항상 짝수라는 조건이 있으므로 홀수인 조건은 신경쓰지 않는다.
a = len(n) // 2 # 왼쪽 부분과 오른쪽 부분의 자릿수(원소 개수)
left = sum(map(int, list(n[:a]))) 
right = sum(map(int, list(n[a:]))) 

if left == right:
    print('LUCKY')
else:
    print('READY')


'''
아래는 책의 코드이다.
원리는 동일하다. (시간 복잡도도 동일하다.)
'''
n = input()
length = len(n) # 점수값의 총 자릿수
summary = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(length // 2):
    summary += int(n[i])

# 오른쪽 부분의 자릿수 합 빼기
for i in range(length // 2, length):
    summary -= int(n[i])

if summary == 0:
    print("LUCKY")
else:
    print("READY")