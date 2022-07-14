# My Solution1(오답, 32개중 6개 시간 초과)
def solution(records):
    
    names = {}                                                          # key: id, value: name으로 이루어진 딕셔너리다.
    result = []                                                         # 해당 기록의 유저 id, 기록을 함께 담을 리스트다.
    
    for record in records:                                              # 모든 기록을 탐색한다.
        record = record.split()
        
        command = record[0]
        if command == 'Enter':
            id, name = record[1], record[2]
            
            if id not in names.keys() or names[id] == name:             # 만약 이전에 들어온 적이 없거나 이전과 동일한 이름으로 들어왔다면
                names[id] = name
                result.append([id, f'{names[id]}님이 들어왔습니다.'])     # 리스트에 저장한다.
                continue
        
            for data in result:                                         # 이전에 모든 기록을 탐색한다.
                data_id = data[0]                                       # 해당 기록의 아이디를 받아온다. 
                if id == data_id:                                       # 만약 들어오려는 아이디와 동일하다면
                    data[1] = data[1].replace(names[id], name)          # 기록의 이름을 바꿔준다.
                                                                        # replace를 없애기 위해 result.append([id, names[id], '님이 들어왔습니다.'])형시으로 바꿔봤지만 동일하게 시간초과가 발생했다.
            names[id] = name                                            # 이전 이름은 사용할 곳이 없으므로 바뀐 이름으로 갱신한다.
            result.append([id, f'{names[id]}님이 들어왔습니다.'])         # 현재 기록을 추가한다.
            
            
        elif command == 'Leave':
            id = record[1]                                              # 해당 명령의 id를 받아온다.
            result.append([id, f'{names[id]}님이 나갔습니다.'])          # 현재 닉네임에 맞게 기록을 추가한다. 
        
        else:
            id, name = record[1], record[2]                             # 닉네임을 바꾸려고 하는 id와 바꾸려고하는 닉네임을 받아온다.
            
            for data in result:                                         # 이전에 모든 기록을 탐색한다.
                data_id = data[0]                                       # 해당 기록의 아이디를 받아온다. 
                if id == data_id:                                       # 만약 들어오려는 아이디와 동일하다면
                    data[1] = data[1].replace(names[id], name)          # 기록의 이름을 바꿔준다.
            names[id] = name                                            # 이전 이름은 사용할 곳이 없으므로 바뀐 이름으로 갱신한다.
            
    answer = [record for _, record in result]
    
    return answer