n = int(input())

count = 0
for a in range(1, 501):
    for b in range(1,501):
        if b<=a and a**2 == (b**2 + n):
            count += 1
print(count)



# n = int(input())
# answer = 0
# for b in range(1,500):
#     for a in range(b,500):
#         if a**2 == b**2+n:
#             answer += 1
# print(answer)



# n = int(input())
# count = 0
# for A in range(1,501):
#     for B in range(1,A):
#         if A**2 - B**2 == n:
#             count +=1
# print(count)



# 시간복잡도
# 몇 번 계산해야하는가?
