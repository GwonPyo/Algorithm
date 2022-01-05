import sys
input = sys.stdin.readline
# 테스트 케이스 입력
test_case = int(input())

# 테스트 케이스 만큼 반복
for _ in range(test_case):
    # 사람수 입력
    n = int(input())
    # 서류 순위와 면접 순위를 입력 받을 리스트 생성
    scores =[]

    # 서류 순위, 면접 순위 입력
    for _ in range(n):
        test1, test2 = map(int, input().split())
        scores.append((test1, test2))

    # 서류 순위로 정렬한다.
    scores.sort()

    # 첫번째 사람은 무조건 합격이므로 result = 1로 초기화한다.
    result = 1
    previous = scores[0]
    for i in range(1, n):
        # 이전에 뽑을 수 있는 사람보다 면접 순위가 높아야만 뽑을 수 있다.
        # 이전에 뽑을 수 있는 사람(previous)는 서류 순위가 무조건 높기 때문에
        # 해당 성적의 사람은 면접 순위가 더 높아야 합격이 가능하다.
        if previous[1] > scores[i][1]:
            result += 1
            previous = scores[i]
    print(result)