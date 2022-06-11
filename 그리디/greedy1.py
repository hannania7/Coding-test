# 최소한의 거스름돈
n = 1260
# 총 연산수행 횟수
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기(몫)
    count += n // coin 
    # 나머지
    n %= coin 
    
print(count)