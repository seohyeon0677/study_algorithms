
# A가 정답으로 생각할 수 있는 모든 수를 넣어보기

# 그리고 B가 도전한 내용에 맞는지 확인하기


n = int(input()) # 4

hint = [list(map(int, input().split())) for _ in range(n)]
# [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]

answer = 0
for a in range(1, 10): # 100의 자리수
    for b in range(1, 10): # 10의 자리수
        for c in range(1, 10): # 1의 자리수
            
            if (a==b or b==c or c==a):
                continue
            
            count = 0
            for arr in hint:
                number = hint[0]
                strike = hint[1]
                ball = hint[2]

                strike_count = 0
                ball_count = 0

                # 자리수를 나눠서 strike, ball count 하는 부분 -> 숙제

                if strike_count == strike and ball_count == ball:
                    count += 1

            if count == n:
                answer += 1

print(answer)
