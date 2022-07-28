# My Solution1
from itertools import combinations_with_replacement
def solution(n, info):
    '''
    n: 쏠 수 있는 화살 수
    info: 어피치가 쏘고 맞춘 점수들의 정보를 모은 정보(리스트)
    '''
    data = [i for i in range(0, 11)]                                    # 점수는 0~10까지 가능하므로 해당 수들을 담은 리스트를 생성한다.
    cbs = list(combinations_with_replacement(data, n))                  # 위에서 만든 리스트를 이용해 중복조합을 만들어 나올 수 있는 점수의 경우를 모두 저장해 놓는다.
    max_gap = 0                                                         # 우리의 목표는 라이언이 승리할 때 라이언과 어피치의 점수차가 최대가 되는 경우이므로 max_gap을 선언한다.
    result = [-1]                                                       # 반환할 리스트를 초기화한다.

    for cb in cbs:                                                      # 모든 점수 조합들을 탐색해본다.
        lion = [0 for _ in range(11)]                                   # 라이언이 쏘고 맞춘 점수들의 정보를 담을 리스트를 선언한다.
        for i in cb:                                                    # 해당 조합에 담겨있는 점수들을 확인하며 리스트에 표시한다.
            lion[i] += 1
        tmp_gap = check_score(lion, info)                               # 라이언과 어피치의 점수차이를 확인한다.

        if tmp_gap > max_gap:                                           # 만약 둘의 차이가 0보다 크거나 이전 최대 gap보다 크다면
            max_gap = tmp_gap                                           # max_gap을 갱신하고 result에 추가한다.
            result = []
            result.append(lion)
        elif tmp_gap == max_gap:                                        # 만약 이전과 차이가 동일하다면
            result.append(lion)                                         # result에 추가한다.
    
    if result[0] == -1:                                                 # 만약 result에 담긴 원소중 첫 번째 원소가 -1 이라면 최대 gap이 0임을 의미한다.
        return [-1]                                                     # 즉, 라이언과 어피치가 비기므로 [-1]을 리턴한다.
    else: 
        return check_result(result)                                     # 만약 라이언이 이기는 경우가 있다면 result의 모든 원소들을 확인하여 가장 최적의 경우를 반환한다.

def check_score(lion, peach):
    result = 0                                                          # lion과 peach의 점수차를 저장할 변수다.
    for i in range(10):                                                 
        if lion[i] - peach[i] > 0: result += (10-i)                     # 만약 해당 점수를 lion이 더 많이 맞췄다면 result에 해당 점수를 더해준다.
        elif lion[i] - peach[i] <= 0 and peach[i] > 0: result -= (10-i) # 만약 peach가 더 많이 맞춘 경우 result에 해당 점수만큼 빼준다.
    return result                                                       # 점수차를 반환한다.

def check_result(results):
    tmp = results[0]                                                    # 최대 차이를 내면서 라이언이 이기는 경우의 수가 results에 담겨있으므로 results의 첫번째 원소를 가져온다.
    
    if len(results) == 1:                                               # 만약 results의 원소가 1개 뿐이라면 
        return tmp                                                      # 첫 번째 원소를 반환한다.
    
    for result in results[1:]:                                          # 모든 경우를 탐색한다.
        for i in range(10, -1, -1):                                     # 더 작은 숫자를 많이 맞춘 경우를 최적의 경우로 보므로 
            if result[i] > tmp[i]:                                      # 만약 이전 경우보다 더 많이 낮은 숫자를 맞추는 경우 tmp에 result를 저장하고
                tmp = result                                            
            if result[i] < tmp[i]:                                      # 이전 경우가 더 적게 낮은 숫자를 맞춘다면 다른 경우를 탐색해야 한다.
                break
    return tmp                                                          # 위 경우를 모두 탐색하고 최적의 경우를 반환한다.

# My Solution2
def solution(n, peach):                                                 
    global max_gap                                                      # 이전 코드처럼 라이언과 피치의 최대 차이를 저장할 변수다.
    global result                                                       # 라이언이 맞출 수 있는 최적의 경우를 저장할 리스트다.
    
    max_gap = 0                                                         # 최대 차이를 0으로 초기화한다.
    result = [-1]                                                       # result는 [-1]로 초기화한다.
    lion = [0 for _ in range(11)]                                       # 라이언의 점수를 저장할 리스트다.
    
    def dfs(depth, ex_num):
        global max_gap                  
        global result
        
        if depth >= n:                                                  # 만약 n번만큼 화살을 쐈다면 
            lion_score, peach_score = check_score(lion, peach)          # lion과 peach의 점수를 계산하고
            gap = lion_score - peach_score                              # 차이를 계산한다.
            
            if gap > 0:                                                 # lion의 점수가 peach보다 높다면
                if gap > max_gap:                                       # 그리고 이전 max_gap보다 더 높다면
                    max_gap = gap                                       # max_gap을 계산하고 result에 해당 경우를 저장한다.
                    result = lion[:]

                elif gap == max_gap:                                    # 이전 max_gap과 동일한 값을 가진다면
                    result = check_result(result, lion)                 # 두 경우중 최적의 경우를 확인하여 result에 저장한다.
            return
        
        for i in range(11):                                             # 아직 화살을 더 쏴야한다면
            if i >= ex_num:                                             # 중복 조합을 계산해야하므로 이전에 쐈던 점수를 쏘지 않는다는 조건을 설정하고
                lion[i] += 1                                            # 백트래킹 방식을 사용하여 탐색한다.
                dfs(depth+1, i)
                lion[i] -= 1
    
    dfs(0, 0)                                                           # 위에서 만든 dfs함수를 실행시킨다.
    
    return result                                                       # 올바른 result값을 반환한다.

def check_score(lion, peach):       
    lion_score = 0                                                      # lion과 peach의 점수를 각각 0으로 초기화한다.
    peach_score = 0
    for i in range(10):                                                 # 10~1점까지 탐색한다.
        if lion[i] > peach[i]:                                          # 만약 lion이 peach보다 해당 점수를 많이 맞춘 경우
            lion_score += (10-i)                                        # lion의 점수에 해당 점수를 더한다.
        else:
            if peach[i] == 0: continue                                  # 만약 peach와 lion 둘다 해당 점수를 맞춘 적이 없다면 다른 점수를 탐색한다.
            peach_score += (10-i)                                       # 만약 peach가 lion보다 더 많이 맞춘 경우 해당 점수를 peach의 점수에 더한다.
    return lion_score, peach_score                                      # lion과 peach의 점수를 반환한다.

def check_result(result, lion):                                         
    for i in range(10, -1, -1):                                         # 0~10점까지 맞춘 화살의 개수를 탐색한다.
        if result[i] > lion[i]:                                         # 만약 이전의 경우(result)가 현재 탐색하는 경우(lion)보다 낮은 점수를 더 많이 맞췄다면
            return result                                               # result를 반환하고
        elif result[i] < lion[i]:                                       # 현재 탐색하는 경우가 이전 경우보다 낮은 점수를 더 많이 맞췄다면
            return lion[:]                                              # lion을 반환한다.