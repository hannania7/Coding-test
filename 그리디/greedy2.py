# 1이 될 때까지
# target : k로 나누어 떨어지는 수
# result : 총 연산수행 횟수

# n, k을 공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0

while True:
    target = (n // k) * k
    # 1을 뺴는 숫자 횟수 result에 더하기    
    result += (n - target)
    n = target
    # n이 k보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누는 횟수 result에 더하기
    result += 1
    n //= k
    
# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)