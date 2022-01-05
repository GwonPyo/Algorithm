import sys
input = sys.stdin.readline

def solution():
    case = int(input())
    answers = []
    for _ in range(case):
        n = int(input())

        # 조건에서 서류 순위와 면접 순위에 동점자는 없다고 했다.
        # 따라서 내가 쓴 코드처럼 서류 순위로 정렬을 하지 않고
        # 면접 순위를 인덱스로 하는 리스트를 만들어 주면된다.
        # 순위는 1 ~ n 까지 이므로 n + 1개 만큼 원소를 만들어 준다.
        scores = [0] * (n + 1)

        for _ in range(n):
            test1, test2 = map(int, input().split())
            scores[test1] = test2
        
        # 인덱스가 1인 원소는 서류 순위가 1등이므로 선발 가능하다.
        # 따라서 result = 1로 초기화 한다.
        result = 1
        min = scores[1]
        # 아래는 내 코드와 원리가 동일하다.
        for score in scores[2:]:
            if(score < min):
                result += 1
                min = score
        
        print(result)

solution()