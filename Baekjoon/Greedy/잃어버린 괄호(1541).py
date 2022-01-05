# 식을 입력 받는다.
formula = input()
# 우리는 첫 번째 -를 기준으로 
# 앞쪽과 뒤쪽으로 나누어 앞의 총합에서 뒤의 총합을 빼주면 된다.
# 입력 받은 식을 -를 기준으로 나눈다.
formula = formula.split('-')
# -를 기준으로 나누었으므로
# formula의 첫번째 문자열(formula[0])이 첫 번째 -의 앞부분이 된다.
# 따라서 formula[0]의 총합을 구한다.
result = sum(list(map(int, formula[0].split('+'))))

# formula[1] 부터 끝까지 각 원소들의 총합을 구해 빼준다.
for i in range(1, len(formula)):
    result -= sum(list(map(int, formula[i].split('+'))))

print(result)