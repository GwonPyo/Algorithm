# 2021.11.03 풀이
import sys 
input = sys.stdin.readline

n = int(input()) # 1 <= 회의 개수(n) <= 100,000
conference_schedule = [] # 회의 정보를 저장할 리스트
# 회의 정보 입력
for _ in range(n):
    conference_schedule.append(tuple(map(int, input().split())))

'''
처음에는 sort를 x[1]만 기준으로 했다. 하지만 x[1]만 기준으로하면 
같은 종료 시간 가진 회의가 여러 개 일때 문제가 발생한다. 
예를 들어, 회의 스케줄들 중에 3이 가장 빨리 종료되는 회의시간이라 가정하자.
근데 3~3, 1~3 순으로 conference_schedule이 정렬되면 1~3은 카운팅되지 않는다. (3(end) > 1(start))
또한 5~5, 4~5 순으로 conference_schedule에 정렬되어 있다면 4~5는 카운팅되지 않는다.
따라서 종료 시간을 기준으로 정렬하고 이후에 시작 시간을 기준으로 다시 정렬해줘야한다.
'''

# 회의 정보를 끝나는 시간을 기준으로 오름차순 정렬을 한다.
conference_schedule.sort(key = lambda x: (x[1], x[0]))

'''
N은 무조건 1개 이상이므로 회의가 0개인 경우의 수는 없다.
따라서 처음 종료 시간이 가장 짧은 회의는 무조건 할 수 있으므로
result의 초깃값은 1로 해준다.
'''
result = 1 # 결과값(result)
start = conference_schedule[0][0]   # 현재 회의의 시작시간(start)
end = conference_schedule[0][1]     # 현재 회의의 종료시간(end)

for index in range(1, n):
    # 현재 회의가 끝나는 시간이 다음 회의의 시작 시간보다 빠르거나 같아야(작거나 같아야)한다.
    if end <= conference_schedule[index][0]:
        result += 1
        start = conference_schedule[index][0]
        end = conference_schedule[index][1]
    
print(result)