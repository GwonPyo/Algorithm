# 2021.11.06 01:31
# my_solution
import sys
input = sys.stdin.readline

'''
총 9명의 난쟁이 중 키의 합이 100인 난쟁이 7명을 골라야 한다. 
9명 중에 7명을 골라 더해주면 반복문이 굉장히 길어진다.
그래서 제외할 2명을 골라주기로 했다.
'''

dwarfs = [] # 난쟁이들의 키를 저장할 리스트
# 키 입력
for _ in range(9):
    dwarfs.append(int(input()))
dwarfs.sort()            # 난쟁이 키 정렬

sum_dwarfs = sum(dwarfs) # 난쟁이 키 총합 저장(sum_dwarfs)
not_dwarf = []           # 난쟁이가 아닌 2명을 저장할 리스트
# 0 ~ 8중 하나의 숫자 선택
for i in range(9):
    # i+1 ~ 8중 하나의 숫자 선택 
    for j in range(i + 1, 9):
        '''
        만약 두 난쟁이를 제외한 합이 100이라면
        not_dwarf 리스트에 저장한다.
        '''
        if sum_dwarfs - (dwarfs[i] + dwarfs[j]) == 100:
            not_dwarf.append((dwarfs[i], dwarfs[j]))

# 7명의 난쟁이를 오름차순으로 출력한다.(이를 위해 미리 정렬한 것이다.)
for dwarf in dwarfs:
    '''
    총합이 100인 경우가 여러 개이면 아무거나 출력해도 된다는 조건이 있다.
    따라서 맨 처음에 발견한 두 명을 사용한다.
    '''
    if dwarf in not_dwarf[0]:
        continue
    print(dwarf)

# other solution

'''
리스트를 만들면서 바로 정렬을 해줬다. 코드가 훨씬 간편한 것 같다.
이 방법을 기억하자.

반복문은 바로 list를 iterator로 사용했다.
이 방법은 딱히 좋진 않은 것 같다.
왜냐하면 총합이 140이고 원소중에 20이 있다면 에러가 발생할 수 있을 것이다.
remove() 함수는 기억해놓자.
하지만 위의 코드에 바로 remove() 함수를 적용하면 반복문에서 indexError가 발생한다.(index가 줄었기 때문이다.)
따라서 반복문 이후에 사용해야 한다.
'''
l = sorted(int(input()) for i in range(9))
for i in l:
    for j in l:
        if i + j == sum(l) - 100:
            l.remove(i)
            l.remove(j)
            break
for i in l:
    print(i)