K, N = map(int, input().split())
lines = list(int(input()) for _ in range(K))

def binary(lines, n):
    left, right = 1, max(lines)
    while left <= right:
        mid = (left + right) // 2

        count = sum(line // mid for line in lines)
        if count >= n:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result

print(binary(lines, N))
