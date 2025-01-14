N = int(input())
A = list(map(int, input().split()))
M = int(input())
Q = list(map(int, input().split()))

A.sort()

def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

for q in Q:
    print(binary_search(A, q))
