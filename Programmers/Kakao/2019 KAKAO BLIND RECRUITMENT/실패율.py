# My Solution
def solution(N, stages):
    failure_rates = []                                                  # 각 스테이지의 실페율을 저장할 리스트다.
    
    for i in range(1, N+1):                                             # 1~N까지 각 스테이지를 확인한다.
        stage_users = 0                                                 # 해당 스테이지에 도달한 인원을 저장할 변수다.
        failure_users = 0                                               # 해당 스테이지에 도달했지만 성공하지 못한 인원을 저장할 변수다.
        for stage in stages:                                            # 각 유저가 머문 스테이지를 확인한다.
            if stage > i:                                               # 만약 해당 stage를 성공한 사람이라면
                stage_users += 1                                        # 스테이지 도달 인원 변수를 갱신한다.
            elif stage == i:                                            # 만약 해당 stage에 머무른 사람이라면
                stage_users += 1                                        # 스테이지 도달 인원 변수와
                failure_users += 1                                      # 실패 인원을 갱신한다.
        if stage_users == 0:                                            # 만약 스테이지에 도달한 인원이 없다면
            failure_rates.append((i, 0))                                # 실패율을 0으로 저장한다.
            continue
        failure_rate = failure_users/stage_users                        # 스테이지 도달인원이 0이 아니라면 실패율을 계산하고 리스트에 넣어준다.
        failure_rates.append((i, failure_rate))
    
    failure_rates.sort(key = lambda item: item[1], reverse=True)        # 실패율을 기준으로 정렬한다.
    
    result = []                                                         # 결과를 저장할 리스트를 선언한다.
    
    for i, _ in failure_rates:                                          # 실패율을 기준으로 정렬된 리스트의 첫번째 원소(스테이지 숫자)를 가져와 result에 넣어준다.
        result.append(i)
    
    return result

# Other Solution
def solution(N, stages):
    result = {}                                                         # 결과를 저장할 딕셔너리를 선언한다.
    users = len(stages)                                                 # 총 유저수를 가져온다.
    for stage in range(1, N+1):                                         # 1~N까지 각 스테이지를 확인한다.
        if users != 0:                                                  # 만약 user수가 0이 아니면 (stage에 도달한 인원이 있다면)
            count = stages.count(stage)                                 # 해당 stage에 있는(아직 성공하지 못한) 인원을 확인하고
            result[stage] = count / users                               # 실패율을 계산한다.
            users -= count                                              # 그리고 이후 스테이지에 도달한 유저를 담기위해 값을 알맞게 조정한다.
        else:
            result[stage] = 0                                           # 만약 스테이지에 도달한 인원이 0명이라면 실패율은 0으로 초기화한다.

    '''
    * sorted(result, key=lambda x : result[x], reverse=True)의 뜻
    sorted에 dict 타입인 result를 넘겨주면 result의 key들이 들어가게 된다.
    Ex) 코드: dict  = {'a': 0, 'b': 1, 'c': 2}; print(sorted(dict)) 결과: ['a', 'b', 'c']
    
    이때 sorted의 key를 value기준으로 정렬하도록 설정했기 때문에 value값으로 key정렬이 가능하다.
    '''
    return sorted(result, key=lambda x : result[x], reverse=True)       # 딕셔너리를 정렬하여 리스트 형태로 반환한다.

