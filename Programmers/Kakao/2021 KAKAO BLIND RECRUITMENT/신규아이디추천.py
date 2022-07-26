# 30분 소요
# My Solution(정답)
def solution(new_id):
    result = ''
    
    # 1. 대문자에서 소문자로 치환
    result = new_id.lower()
    
    # 2. 알파벳 소문자, 숫자, -, _, .를 제외한 모든 문자 제거
    # 3. 2번이상 연속된 .은 하나의 .으로 치환
    tmp = ''
    for i in result:
        if 'a'<=i<='z' or '0'<=i<='9' or i=='-' or i=='_':
            tmp += i
        elif i=='.':
            if len(tmp)==0: tmp += '.'
            elif tmp[-1]!='.': tmp += '.'
    result = tmp
    
    # 4. 처음과 끝에 위치한 .제거
    result = result.strip('.')
    
    # 5. 빈 문자열이면 a대입
    if len(result)==0: result += 'a'
    
    # 6. 길이가 16이상이면 15개의 무자만 남김. 끝에 .있으면 제거
    if len(result)>=16: 
        result = result[:15]
        result = result.rstrip('.')
    
    # 7. 길이가 2이하면 new_id의 마지막 문자를 길이가 3이 될 때까지 반복
    if len(result)<=2:
        result += result[-1]*(3-len(result))
    
    return result

# Other Solution + My Solution
def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    result = ''
    for word in new_id:
        if word.isalnum() or word in '-_.': 
            '''
            string.isalpha: 영어 혹은 한글로 이루어진 문자열인 경우 True 반환
            string.isalnum: 숫자, 영어 혹은 한글로 이루어진 문자열인 경우 True 반환
            '''
            result += word
    # 3단계
    while '..' in result: result = result.replace('..', '.')
    
    # 4단계
    result = result.strip('.')
    
    # 5단계
    result = 'a' if result == '' else result
    
    # 6단계
    if len(result)>=16: 
        result = result[:15]
        result = result.rstrip('.')
    # 7단계
    if len(result)<=2:
        result += result[-1]*(3-len(result))
        
    return result