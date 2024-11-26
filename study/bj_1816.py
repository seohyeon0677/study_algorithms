TC = int(input()) # TestCase 개수

for _ in range(TC):
    number = int(input()) # TestCase

    for i in range(2, 1000001): # 2 ~ 100만 반복
        if number % i == 0: # 100만 이하의 약수 존재
            print("NO")
            break
        if i == 1000000: # 100만 이하의 약수 존재 X
            print("YES")
