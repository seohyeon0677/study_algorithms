# 입력을 받고 ( 디테일! )

# Default input : String 타입, 문자열 타입으로 받아오도록 만들어짐!

# 배열!
# list = [0,0,0,0]
# list = ["he", "hi", "hu"]


# Case 1 : 단순히 정수일 때
# number = int(input())

# Case 2 : 수열
list1 = list(map(int, input().split()))

print(*list1)

# Case 3 : 단순히 문자일 때
# string = input() #12


# Case 4 : 문자열
list2 = list(map(str, input().split()))

print(*list2)


# 계산을 하고


# 출력을 한다
# print(number + number) # 24
# print(string + string) # 1212


# 1 2 3
# [1, 2, 3]
# A B C
# ['A', 'B', 'C']

# *를 붙이면 그대로 출력
# 1 2 3
# 1 2 3
# A B C
# A B C



##### 강의노트 #####

# 숫자를 입력 받을 때는 int(input())
# 문자를 입력 받을 때는 input()
# 여러 가지 숫자들의 조합; 수열 -> list(map(int, input().split()))
# 여러 가지 문자들의 조합; 문자열 -> list(map(str, input().split()))
