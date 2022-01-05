# My Solution(100ms)
from itertools import permutations
'''
그냥 permuatations 함수를 사용해
모든 순열의 경우를 구해주고 출력해줬다.
'''
n = int(input())                        # 1 ≤ N ≤ 8
data = list(map(str, range(1, n+1)))    # 1~n까지의 숫자를 str형으로 변환해 data에 저장한다. 
                                        # 변형하지 않으면 나중에 str형으로 리스트 한 개에 한 번씩 변형해야 하므로 비용이 증가한다. 
pms = list(permutations(data, n))       # 모든 순열을 구해 리스트에 저장한다.

for i in range(len(pms)):               # 모든 순열을 출력한다.
    print(' '.join(pms[i]))             # print(*pms) 사용시 148ms로 비용이 증가한다.

# My Solution(96ms)
'''
다른 사람 코드에서 sys.stdout.write를 사용했길래 사용해봤다.
시간상에 차이는 많이 없는 것 같다.
단, print()처럼 개행을 자동으로 해주지 않으므로 '\n'을 붙여줬다.
'''
import sys
from itertools import permutations
print = sys.stdout.write

n = int(input())
data = list(map(str, range(1, n+1)))

pms = list(permutations(data, n))

for i in range(len(pms)):
    print(' '.join(pms[i]) + '\n')