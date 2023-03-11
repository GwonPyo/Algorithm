import sys
input = sys.stdin.readline
INF = float("inf")

city_num = int(input())
bus_num = int(input())
results = [[INF for _ in range(city_num)] for _ in range(city_num)]

for city in range(city_num):
    results[city][city] = 0

for _ in range(bus_num):
    start_city, end_city, cost = map(int, input().split())
    results[start_city-1][end_city-1] = min(results[start_city-1][end_city-1], cost)

for mid_city in range(city_num):
    for start_city in range(city_num):
        for end_city in range(city_num):
            tmp = results[start_city][mid_city]+results[mid_city][end_city]
            results[start_city][end_city] = min(results[start_city][end_city], tmp)
    
for result in results:
    for i in range(city_num):
        if result[i] == INF:
            result[i] = 0

for result in results:
    print(*result)