# My Solution
from itertools import combinations
from collections import defaultdict

def solution(orders, courses):
    '''
    orders: 각 손님들이 주문한 단품요리를 문자열 형태로 저장한 리스트 
    courses: 코스 요리를 몇 개의 단품 요리로 구성할지에 대한 숫자가 들어있는 리스트
    '''
    for i in range(len(orders)):                                                                # 반환할 리스트(result)에 들어갈 문자열은 모두 정렬되어 있어야 한다. (BA(x) / AB(o))
        orders[i] = sorted(orders[i])                                                           # 따라서 orders에 들어있는 문자열들은 미리 정렬되어 있어야 이후 combinations 등의 함수를 쓸때 편하다.
    
    result = []                                                                                 # 반환할 리스트를 선언한다.
    
    for course in courses:                                                                      # courses에는 몇 개의 단품 요리로 구성할지에 대한 숫자가 들어있다.
        combs_dict = defaultdict(int)                                                           # 이후 값 갱신하기 편하게 하기 위해 defaultdict를 선언한다.
        
        for order in orders:                                                                    # 각 주문들을 확인한다.                                 
            combs = list(combinations(order, course))                                           # 해당 주문에서 개수에 맞는 조합을 뽑는다. 
            for comb in combs:                                                                  # 각 조합의 value값에 1을 더한다.
                combs_dict[comb] += 1
                
        combs_list = sorted(combs_dict.items(), key = lambda item: item[1], reverse = True)     # 위에서 만든 defaultdict값을 정렬한다.
        
        if len(combs_list) == 0 or combs_list[0][1] < 2:                                        # 만약 defaultdict를 정렬한 list가 비어있거나 가장 많이 나온 조합이 2번 이상 주문되지 않으면 위로 올라간다.
            continue
        
        result.append(''.join(combs_list[0][0]))                                                # 처음 원소의 문자열을 저장한다.
        max_num = combs_list[0][1]                                                              # 처음 원소의 정숫값을 저장한다.
        
        for i in range(1, len(combs_list)):                                                     # 리스트의 이후 원소들을 탐색한다.
            if combs_list[i][1] < max_num:                                                      # 만약 처음 문자열(조합)보다 주문된 횟수가 적다면
                break                                                                           # 반복문을 탈출한다.
            result.append(''.join(combs_list[i][0]))                                            # 처음 문자열(조합)보다 주문된 횟수가 동일하면 result에 추가한다.
        
    result.sort()
    
    return result

# Other Solution
from itertools import combinations
from collections import Counter

def solution(orders, courses):
    answer = []
    
    for course in courses:
        array = []                                              # 개수(course)에 맞는 조합을 모두 저장할 리스트다.
        for order in orders:
            order = sorted(order)                               # 위에서 내코드와 같은 원리로 미리 order를 정렬한다.
            array.extend(list(combinations(order, course)))     # 주어진 개수에 맞는 조합을 뽑아내고 array에 추가한다.
        
        count = Counter(array)                                  # array에 중복된 원소들의 값들을 세어준다.
        
        if count:                                               # count에 원소가 존재하고
            if max(count.values()) >= 2:                        # 가장 많이 주문된 조합의 횟수가 2회 이상이라면
                for key, value in count.items():                # 모든 조합을 탐색하여
                    if value == max(count.values()):            # 해당 조합의 주문 횟수가 최대 주문 횟수와 같다면
                        answer.append("".join(key))             # 반환할 리스트(answer)에 추가해준다.
    
    return sorted(answer)