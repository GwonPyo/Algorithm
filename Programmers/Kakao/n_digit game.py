def solution(n, t, m, p):
    # n: 진법, t: 미리 구할 숫자의 갯수, m: 게임 참가 인원, p: 튜브 순서
    
    answer = ''                            # 출력값을 담을 문자열이다.
    str_list = ''                          # 모든 사람틀(m)이 t개 이상의 숫자(문자)를 불렀을 때 지금까지 나온 문자를 저장해 놓은 문자열이다. 
    
    count = 0                              # 현재 사람들이 외쳐야할 숫자를 의미한다.
    while len(str_list) < t*m:
        str_list += conversion(n, count)   # count를 n진법으로 변환하고
        count += 1                         # 다음 숫자를 탐색할 수 있도록 갱신한다.
    
    count = 0                              # 위에서 생성한 str_list에서 t개의 올바른 문자를 뽑아야 한다.
    while len(answer) < t:
        answer += str_list[count*m+p-1]    # 알맞은 인덱스에 접근해서 answer에 넣어준다.
        count+=1                           # count에 1을 더해서 이후에도 올바른 인덱스에 접근할 수 있게 한다.
    
    return answer

def conversion(n, number):
    result = ''
    while number >= n:                     # number가 나눠야할 수인 n보다 크거나 같다면 반복문을 수행한다.     
        tmp = number%n                     # number를 n으로 나눴을 때 나머지를 tmp에 저장하고 몫은 number에 저장한다.
        number = number//n
        if tmp < 10:                       # tmp(나머지)가 10보다 작다면 해당 숫자를 문자열로 변환해 result의 맨 앞부분에 저장한다.
            result = str(tmp)+result
        else:  
            result = chr(65+tmp-10)+result # tmp(나머지)가 10보다 크다면 올바른 알파벳을 result의 맨 앞부분에 저장한다.
    
    if number < 10:                        # 마지막으로 number에 저장된 값을 위와 동일한 방식으로 result 맨 앞부분에 추가해준다.
        result = str(number)+result
    else:  
        result = chr(65+number-10)+result
        
    return result
            
    
