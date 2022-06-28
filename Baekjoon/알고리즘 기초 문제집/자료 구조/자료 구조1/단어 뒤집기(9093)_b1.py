import sys
input = sys.stdin.readline

# My Solution(164ms)
'''
풀이 과정 예시) 
1. I am happy today 입력
2. I, am, happy, today를 각각 리스트로 만듬. -> [['I'], ['a','m'], ['h','a','p','p','y'], ['t','o','d','a','y']]
3. 각각의 리스트를 reverse시키고, join함수를 이용해 문자열로 이어줌. -> ['I', 'ma', 'yppah', 'yadot']
4. 각 문자열을 join함수로 다시 합쳐서 새로 만든 문자열 반환함. -> I ma yppah yadot
'''
for _ in range(int(input())):
    string = map(list, input().split())
    changed_string = []
    
    for i in string:
        i.reverse()
        changed_string.append(''.join(i))
    
    print(' '.join(changed_string))
    
# Other Solution(104ms)
'''
풀이 과정 예시) 
1. I am happy today 입력
2. 입력과 동시에 해당 문자열을 reverse 시킴. -> yadot yppah ma I
3. 해당 문자열을 list를 만들고, reverse 시킴. -> ['I', 'ma', 'yppah', 'yadot']
4. join 함수를 사용해 합치고 만들어진 문자열 반환함. -> I ma yppah yadot
'''
for i in range(int(input())):
    string = input()[::-1]
    string = string.split()
    string.reverse()
    string = ' '.join(string)
    print(string)