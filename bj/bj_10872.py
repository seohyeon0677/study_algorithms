def factorial(n, current_result=1):
    if n == 0:
        return current_result
    return factorial(n - 1, current_result * n)

n = int(input())

print(factorial(n))
