# 20분 소요
# My Solution(정답)
def solution(id_list, report, k):
    id_index = {}                                       # 각 id의 인덱스를 저장할 딕셔너리 (인덱스는 이후 모든 배열에서 해당 id의 인덱스가 됨)
    reported_list = [[] for _ in range(len(id_list))]   # 각 사람을 신고한 사람을 저장할 리스트 (즉, a가 b를 신고할 경우 b의 리스트에 a를 저장함)
    
    for index, id in enumerate(id_list):
        id_index[id] = index                            # 각 id에 맞는 index를 딕셔너리에 넣어줌
        
    for string in report:
        a, b = string.split()                           # 신고자, 대상자를 받아옴
        a, b = id_index[a], id_index[b]                 # 신고자, 대상자에 해당하는 index를 받아옴
        
        if not a in reported_list[b]:                   # 만약 신고자가 이전에 해당 인원을 신고한적이 없다면
            reported_list[b].append(a)                  # 리스트에 해당 신고자를 추가함
    
    result = [0 for _ in range(len(id_list))]           # 함수에서 반환할 리스트 초기화
    
    for i in range(len(id_list)):                       
        if len(reported_list[i]) >= k:                  # 만약 해당 인원이 신고받은 수가 제한된 수(k)를 넘었다면
            for j in reported_list[i]:                  # 해당 인원을 신고한 사람들의 결과값에 1을 더해준다.
                result[j] += 1
    
    return result

# Other Solution
from collections import defaultdict

def solution(id_list, report,k):
    result = []
    report = list(set(report))                          # 내 코드에서는 report에 중복된 경우를 고려했지만 해당 코드는 미리 이러한 경우를 제거함
    report_dict = defaultdict(set)                      # 각 id가 신고한 사람들의 id를 가진 set을 저장할 딕셔너리
    count = defaultdict(int)                            # 각 id당 신고당한 횟수를 저장할 딕셔너리
	
    for r in report:                                    
        a,b = r.split()
        report_dict[a].add(b)                           # a(신고자)를 id로 가지고 해당 id와 맵핑되는 리스트에 b(대상자)를 넣어줌
        count[b] += 1                                   # b(대상자)의 count값에는 1을 더해줌.
    
    for i in id_list:                                   # 각 id를 불러옴.
        tmp = 0                          
        for j in report_dict[i]:                        # 만약 해당 id가 신고한 사람이
            if count[j]>=k:                             # k번 이상 신고당했다면
                tmp +=1                                 # 값에 1을 더해줌.
        result.append(tmp)                              # 결과값을 result에 넣어줌.
    return result