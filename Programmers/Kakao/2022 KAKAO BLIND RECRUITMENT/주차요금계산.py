from math import ceil
from collections import defaultdict

def solution(fees, records):
    '''
    fees: [기본 시간, 기본 요금, 단위 시간, 단위 요금] 정보가 저장된 리스트 / 기본 시간과 단위 시간의 단위는 분
    records: 차량들의 입출 정보가 담긴 리스트로 [입출 시간, 차량 번호, 입출 정보]가 담김
    '''
    base_time, base_fee, unit_time, unit_fee = fees                                 # fees에 담긴 정보를 이후에 사용하기 쉽게 변수에 담아준다.
    check_in_dict = {}                                                              # 차량들이 들어온 시간을 체크하기 위해 딕셔너리를 선언한다.
    check_out_dict = defaultdict(int)                                               # 차량들이 나갈 때 들어온 시간과의 차이를 넣어줄 딕셔너리다.
    
    for record in records:                                                          # 모든 입출력 정보를 확인한다.
        time, num, status = record.split()                                          # 시간, 차량 번호, 입출 정보를 가져온다.
        hour, minute = map(int, time.split(':'))                                    # 시간의 경우 '06:30'처럼 문자열로 되어있으므로 시간과 분으로 나눠 int형으로 변환해준다.

        if status == 'IN':                                                          # 차량이 들어왔다면
            check_in_dict[num] = hour*60+minute                                     # 차량이 들어온 시간을 분으로 환산해서 check_in_dict에 넣어준다.
            
        else:                                                                       # 차량이 나간다면
            in_time = check_in_dict[num]; out_time = hour*60+minute                 # 차량이 들어온 시간과 나간 시간을 분으로 치환한 값들을 가져오고
            check_out_dict[num] += out_time-in_time                                 # 해당 값의 차이를 check_out_dict에 넣어준다.
            del check_in_dict[num]                                                  # 해당 차량이 들어왔던 정보를 삭제한다.
    
    out_time = 23*60+59                                                             # 만약 들어오고 나가지 않은 차량이 있다면 출차된 시간을 23:59으로 간주한다.
    for num, in_time in check_in_dict.items():                                      # 이전과 같은 방식으로 check_out_dict의 값을 갱신한다.
        check_out_dict[num] += out_time-in_time
    
    result = []                                                                     # 반환할 리스트를 선언한다.
    check_out_list = sorted(check_out_dict.items(), key=lambda x:x[0])              # key를 기준으로 item들을 정렬한다.
        
    for _, time in check_out_list:                                                  # 정렬한 item들의 value(time)값을 받아온다. (차량 번호를 기준으로 정렬된 이후에는 차량 번호를 쓰지 않으므로 가져올 필요가 없다.)
        fee = base_fee + ceil(check_num(time-base_time)/unit_time) * unit_fee       # 요금을 계산한다.
        result.append(fee)                                                          # 계산된 요금을 result에 추가한다.
    
    return result

def check_num(num):                                                                 
    '''
    0 또는 양수는 그냥 반환하고, 음수는 0을 반환하는 함수다.
    '''
    if num >= 0:
        return num
    else:
        return 0
    
