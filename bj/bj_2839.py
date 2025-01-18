def sugar(N):
    for five in range(N//5, -1, -1):
        need = N - (five * 5)
        if need % 3 == 0:
            three = need // 3
            return five + three
    return -1

N = int(input())
print(sugar(N))
