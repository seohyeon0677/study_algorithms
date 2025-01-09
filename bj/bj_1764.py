import sys
input = sys.stdin.read

# 입력 처리
data = input().split()
N, M = map(int, data[:2])
L = set(data[2:2 + N])
S = set(data[2 + N:])

# 교집합 계산 및 정렬
LandS = sorted(L & S)

# 출력
sys.stdout.write(f"{len(LandS)}\n")
sys.stdout.write("\n".join(LandS) + "\n")
