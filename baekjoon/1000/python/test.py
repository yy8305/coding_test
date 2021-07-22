import time

def solution(a, b):
	print(a + b)

a ,b = map(int, input().split())

start = time.time()  # 시작 시간 저장
solution(a, b)

print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간