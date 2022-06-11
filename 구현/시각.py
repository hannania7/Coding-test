h = int(input())

count = 0
# 시 분 초
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str[i] + str[j] + str[k]:
                count += 1
                
print(count)