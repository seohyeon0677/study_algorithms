# Sol 1
# import math

# a, b = map(int, input().split())

# gcd = math.gcd(a, b)    # 최대공약수 계산
# lcm = a * b // gcd      # 최소공배수 계산

# print(gcd)
# print(lcm)


# Sol 2
# 최대공약수 구하는 함수 (유클리드 호제법)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 최소공배수 구하는 함수
def lcm(a, b):
    return a * b // gcd(a, b)

# 두 수 입력받기
a, b = map(int, input().split())

# 최대공약수와 최소공배수 계산
print(gcd(a, b))
print(lcm(a, b))
