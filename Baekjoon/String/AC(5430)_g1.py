# My Solution1(시간초과)
'''
숫자를 입력받고,
R, D 명령에 따른 수행을 하도록 구현하려고 했다.
R: 배열에 있는 숫자의 순서를 뒤집는다.
D: 첫 번째 숫자를 버린다. 배열이 비어있는 경우 에러가 발생한다.
'''
import sys
from collections import deque
input = sys.stdin.readline

for i in range(int(input())):
    commands = list(input().rstrip())                               # 1 ≤ commands ≤ 100,000
    n = int(input())                                                # 0 ≤ n ≤ 100,000
    datas = deque([])
    if n > 0:
        datas = deque(map(int, input().strip('[]\n').split(',')))   # 1 ≤ xi ≤ 100
    else:
        input()

    check = 0                                                       # 비어있는 리스트(큐)에서 pop동작을 수행했는지 확인하기 위한 변수다.
    for command in commands:
        if command == 'R':                                          # 명령이 R인 경우 리스트(큐)를 뒤집는다.
            '''
            reverse() 함수의 시간 복잡도: O(n)
            모든 명령이 R인 경우 시간 복잡도: O(n^2)
            따라서 해당 코드는 시간 초과가 발생한다.
            '''
            datas.reverse()
        else:                                                       # 명령이 D인 경우
            if len(datas) == 0:                                     # 리스트(큐)에 숫자가 없다면 check를 갱신하고 반복문을 종료한다.
                check = -1
                break

            datas.popleft()                                         # 리스트의 첫 번째 원소를 삭제한다.

    if check == -1: print('error')                                  # 원소가 없는 리스트(큐)에서 D명령을 수행한 경우 error를 출력한다.
    else: print('[' + ','.join(map(str, datas)) + ']')              # 남아있는 원소를 출력한다.

# My Solution2(232ms)
'''
이전에 시간초과에서 문제가 되었던 reverse() 함수 대신에 다른 방식을 사용했다.
R명령을 수행하면, 이전에 끝에 있던 원소가 다음 R명령의 대상이 된다.
따라서 임의의 변수(pop_index)를 사용해 리스트의 첫 번째 원소 또는 마지막 원소가 D 명령의 대상이 되는지
확인하면 reverse() 함수를 사용하지 않고 popleft(), pop() 함수를 이용해 원소를 삭제할 수 있다.
단, 출력할 때는 해당 변수를 기준으로 출력해야 한다.

또한 개선한 점이 하나 더있다.
이전에는 숫자를 정수형으로 바꿔줬지만 사실 그럴 이유가 전혀 없다.
따라서 그냥 str형으로 코드를 작성했다.
'''
import sys
from collections import deque
input = sys.stdin.readline

for i in range(int(input())):
    commands = list(input().rstrip())                       # 1 ≤ commands ≤ 100,000
    n = int(input())                                        # 0 ≤ n ≤ 100,000
    datas = []                          
    if n > 0:
        datas = deque(input().strip('[]\n').split(','))     # 1 ≤ xi ≤ 100
    else:
        input()
    
    pop_empty_list = False                                  # 비어있는 리스트(큐)에서 pop동작을 수행했는지 확인하기 위한 변수다.
    pop_index = 1                                           # 뒤에 있는 원소를 뺄지, 앞에 있는 원소를 뺄지 결정하기 위한 변수다.
    for command in commands:
        if command == 'R':                                  # 명령이 R인 경우 pop_index의 부호를 반대로 바꿔준다.
            pop_index *= -1
        else:                                               # 명령이 D인 경우 
            if len(datas) == 0:                             # 리스트(큐)에 숫자가 없다면 pop_empty_list를 갱신하고 반복문을 종료한다.
                pop_empty_list = True
                break

            if pop_index == 1:                              # 첫 번째 원소가 대상이라면 popleft() 함수를 수행한다.
                datas.popleft()
            else:                                           # 마지막 원소가 대상이라면 pop() 함수를 수행한다.
                datas.pop()

    if pop_empty_list: print('error')                       # 원소가 없는 리스트(큐)에서 D명령을 수행한 경우 error를 출력한다.
    elif pop_index == 1: print('[' + ','.join(datas) + ']') # 뒤집혀 있는 상태가 아니라면 남아있는 원소를 출력한다.
    else: print('[' + ','.join(reversed(datas)) + ']')      # 뒤집혀 있는 상태라면 리스트(큐)를 뒤집고 남아있는 원소를 출력한다.

# Other Solution(188ms)
'''
이전에 내가 사용했던 풀이는 pop() 함수를 이용했다.
하지만 D를 이용할 때마다 pop을 수행하는 것보다, 몇 개의 수를 뽑아야 하는지 확인하고 한 번에 뽑아주는 것이
컴퓨터 입장에서는 훨씬 빠르게 수행이 가능하다.

아래 코드는 이전과 동일하게 R 명령에서는 변수 하나를 정해서 다음 삭제할 대상의 위치를 변경해준다.
하지만 D 명령의 경우 각 케이스에 알맞는 변수를 갱신한다.
즉, 왼쪽을 빼야하면 왼쪽에서 삭제할 원소의 개수를 추가해주고
오른쪽에서 빼야하면 오른쪽에서 삭제할 원소의 개수를 추가해야 한다.

그리고 출력시에는 왼쪽에서 뺄 원소의 개수와 오른쪽에서 뺄 원소의 개수를 더해
입력받은 숫자의 개수보다 많으면 error를 출력하고 아니라면, 올바른 결과를 출력해준다.

추가적으로 개선된 점이 있는데
명령을 입력받을 때 RR은 모두 지워준다는 것이다.
사실 R을 두 번하면 아무 의미도 없기 때문에 미리 지우면 이후에 리스트(commands)의 원소를 확인할 때 더 빠르게 수행이 가능할 것이다.
(생각해봤는데, RR을 찾는 시간이나, 그냥 모든 원소를 다 찾는 시간이나 별다른 차이가 없을 것 같다.
실제로 해당 코드를 삭제하고 돌려봤는데 동일하게 188ms가 나왔다.)
'''
import sys
input = sys.stdin.readline

for i in range(int(input())):
    commands = list(input().rstrip().replace('RR', ''))         # 1 ≤ commands ≤ 100,000
    n = int(input())                                            # 0 ≤ n ≤ 100,000
    datas = list(input().strip('[]\n').split(','))              # 1 ≤ xi ≤ 100
    if n == 0: datas = []

    left, right, pop_index = 0, 0, 1                            # 왼쪽, 오른쪽에서 삭제할 원소의 개수, 삭제할 대상을 정해주는 변수다.

    for command in commands:                                    # commands의 모든 원소를 탐색한다.
        if command == 'R': pop_index *= -1                      # 명령이 R인 경우 pop_index의 부호를 반대로 바꿔준다.
        else:
            if pop_index == 1: left += 1                        # 왼쪽에서 원소를 빼야하면 left에 1을 더해준다.
            else: right += 1                                    # 오른쪽에서 원소를 빼야하면 right에 1을 더해준다.

    if left+right <= n:                                         # 빼야할 원소의 개수가 리스트의 원소 개수보다 크거나 같으면
        result = datas[left:n-right]                            # 결과를 담은 리스트다.
        if pop_index == 1: print('[' + ','.join(result) + ']')  # 뒤집혀 있는 상태가 아니라면 남아있는 원소를 출력한다.
        else: print('[' + ','.join(result[::-1]) + ']')         # 뒤집혀 있는 상태라면 남아있는 원소를 거꾸로 출력한다.
    
    else:                                                       # 원소가 없는 상태에서 D명령을 수행하므로 error을 출력한다.
        print('error')                                          